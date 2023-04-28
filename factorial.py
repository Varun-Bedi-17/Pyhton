def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

num=6
print("factorial is",fact(num))
'''Built in Function----math.factorial(num)
                        import math'''