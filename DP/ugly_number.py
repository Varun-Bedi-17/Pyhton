#       Ugly numbers - Those numbers whose prime factorisation include 2,3 and 5 only.

# --------------------------------- Basic Approach

def maxDivisible(a, b):
    while a%b == 0:
        a = a//b
    return a

def chckUgly(number):
    number = maxDivisible(number,2)
    number = maxDivisible(number,3)
    number = maxDivisible(number,5)

    return 1 if number == 1 else 0


def uglyNumber(n):
    i = 1 
    uglyCount = 1

    while n > uglyCount:
        i += 1
        if chckUgly(i):
            uglyCount += 1

    return i


# print(uglyNumber(10))




# ------------------------------------------ DP

def uglyDp(n):
    dp = [1 for _ in range(n)]

    multiple2,multiple3,multiple5 = 0,0,0

    for i in range(1,n):
        dp[i] = min(dp[multiple2]*2, dp[multiple3]*3, dp[multiple5]*5)

        if dp[i] == dp[multiple2]*2:
            multiple2 += 1

        if dp[i] == dp[multiple3]*3:
            multiple3 += 1

        if dp[i] == dp[multiple5]*5:
            multiple5 += 1

    # print(dp)
    return dp[-1]
    
# print(uglyDp(10))





# ----------------------------------------- Binary Search