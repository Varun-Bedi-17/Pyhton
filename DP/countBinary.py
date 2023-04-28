#       Count binary strings without consecutive 1's

# ---------------------------------- Basic Approach

def countBin(n, lastdigit=0):
    if n == 0:
        return 0

    if n==1:
        return 1 if lastdigit==1 else 2

    if lastdigit == 0:
        return countBin(n-1, 0) + countBin(n-1, 1)

    else:
        return countBin(n-1, 0)


# N = 3    # [000, 001, 010, 100, 101]  == 5
# print(countBin(2))


#  -------------------------------------    Another method

def countBinary(n):
    ones = [0 for i in range(n)]
    zeroes = [0 for i in range(n)]

    ones[0] = zeroes[0] = 1

    for i in range(1,n):
        zeroes[i] = ones[i-1] + zeroes[i-1]
        ones[i] = zeroes[i-1]

    return (zeroes[n-1]+ones[n-1])

# N = 3    # [000, 001, 010, 100, 101]  == 5
# print(countBinary(5))      # but this approach is wrong fir N >=43


#    ------------------  Fibonacci Approach (this also gives wrong for N>=43)

def countBin_fibo(n):
        a = 1
        b = 1
        i = 1
        while (i < n) :
            temp = a + b
            b = a
            a = temp
            i += 1
        return a + b

# N = 3
# print(countBin_fibo(N))


# ---------------------------------------------  DP
def countStrings(n):
 
    T = [[0 for x in range(2)] for y in range(n + 1)]
 
    # if only one digit is left
    T[1][0] = 2
    T[1][1] = 1
 
    for i in range(2, n + 1):
 
        # if the last digit is 0, we can have both 0 and 1 at the current position
        T[i][0] = T[i-1][0] + T[i-1][1]
 
        # if the last digit is 1, we can have only 0 at the current position
        T[i][1] = T[i-1][0]
 
    return T[n][0]

# N = 43 
# print(countStrings(N))



# ----------------------------------  GFG(for n>= 43)
# In gfg they asked solution to modulo of 10**9+7. So, we have to do this

def countStrings_gfg(n):
    MOD = 10**9 + 7
    a=[0 for i in range(n)]
    b=[0 for i in range(n)]
    a[0] = b[0] = 1
    for i in range(1,n):
        a[i] = (a[i-1]%MOD + b[i-1]%MOD )%MOD
        b[i] = a[i-1] %MOD
    return (a[n-1]% MOD + b[n-1]%MOD ) %MOD


# print(countStrings_gfg(43))



#  --------------- Print All

def printStr(n, out='',l =[],  last_digit=0):
    if n == 0:
        l.append(out)
        # print(out, end=" ")
        return
 
    printStr(n - 1, out + '0', l,  0)
 
    if last_digit == 0:
        printStr(n - 1, out + '1', l, 1)

    return l
N = 5
print(printStr(N))