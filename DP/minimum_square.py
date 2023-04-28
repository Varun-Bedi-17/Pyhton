# -----------------------------------------Simple but wrong approach

# def minSquare(n):
#     count = 0
#     while n !=0 :
#         if n <= 3:
#             count += n
#             break
#         else:
#             i = 2
#             while i*i <= n:
#                 i += 1
            
#             i = i-1
#             count += 1
#             n = n-(i*i)

#     return count


# n = 13
# print(minSquare(n))
# n1 = 12
# print(minSquare(n1))      # Output is 4 but it is wrong as 4+4+4=12, so output must be 3. Also wrong for n=19(must be 3 but give 4)



#  -----------------------------------Recursion

# def minSquare_recur(n):
#     if n <= 3:
#         return n
    
#     var = n
#     i = 1
#     while (i*i)<=n:
#         var = min(var,1+minSquare_recur(n-(i*i)))
#         i += 1

#     return var

# print(minSquare_recur(12))


#------------------------------------Memoization


# def minSquare_memo(n):
#     def recurse(n):

#         if d[n] != -1:
#             return d[n]

#         if n <= 3:
#             d[n] = n
        
#         var = n
#         i = 1
#         while (i*i)<=n:
#             var = min(var,1+recurse(n-(i*i)))
#             i += 1
#         d[n] = var

#         return d[n]
#     d = [-1]*(n+1)          # Creation of memo list
#     return recurse(n)

# print(minSquare_memo(1024))           #  Acceptable in leetcode


## ---------------------------------Memoization another method
# import sys

# def numSquares(n):
#         def recurse(n):

#             if d[n] != sys.maxsize:
#                 return d[n]

#             elif n <= 3:
#                 d[n] = n

#             i = 1
#             while (i*i)<=n:
#                 d[n] = min(d[n],1+recurse(n-(i*i)))
#                 i += 1

#             return d[n]
        
#         d = [sys.maxsize]*(n+1)
#         return recurse(n)


# print(numSquares(98))





#--------------------------------   DP

def minSquare_dp(n):
    T = [0] * (n + 1)
 
    for i in range(n + 1):
 
        T[i] = i
 
        j = 1
        while j*j <= i:
            T[i] = min(T[i], 1 + T[i - j*j])
            j += 1
 
    return T[n]

print(minSquare_dp(5))