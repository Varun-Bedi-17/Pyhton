###########                       Add all numbers till n                   ###############

# def addNumbr(n):
#     if n == 0:
#         return n
#     return n + addNumbr(n-1)

# print(addNumbr(56))
# --------------------------------------------------------------------------------------------------------------
# def addNumbr(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum

# print(addNumbr(56))




###########                            Calculate n raised to power p                             ###############

# def power(n,p):
#     if p == 0:
#         return 1
#     return n * power(n,p-1)

# print(power(5,6))

# print(5**6)
# print(pow(5,6))




##########                          Factorial of a number n                        ######################

# from math import factorial


# def fac(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * fac(n-1)

# print(fac(37))

# print(factorial(37))       #  Function of math




################                     nth fibonacci number                    ###################


# def fibo(n):
#     if n == 0 or n==1:
#         return n
#     return fibo(n-1) + fibo(n-2)

# print(fibo(35))

#  -----------------------------------------------------------------------------------------------

# def fibo(n):
#     if n ==0 or n == 1:
#         return n
#     first = 0
#     second = 1

#     for i in range(2,n+1):
#         number = first + second
#         first = second
#         second = number
#     return number

# print(fibo(16))