
def friends_pair(n):
    return n if n<=2 else friends_pair(n-1) + (n-1)*friends_pair(n-2)

# print(friends_pair(3))


# ----------------------------------- Memoization
def friendsPairMemo(n):
    global memo       # Takes memo which is declared globally
    if n in memo:
        return memo[n]
    
    if n > 2:
        memo[n] = friendsPairMemo(n-1) + (n-1) * friendsPairMemo(n-2)

    else:
        memo[n] = n
    
    return memo[n]

memo = {}
# print(friendsPairMemo(4))



# ----------------------------------------- DP
def friendsPairDp(n):
    dp = [0 for _ in range(n+1)]
    for i in range(n+1):
        if i <= 2:
            dp[i] = i
        else:
            dp[i] = dp[i-1] + (i-1)*dp[i-2]
    return dp[n]

# print(friendsPairDp(4))




# -------------------------------------- Fibonacci

def friendPairFibo(n):
    if n<=2:
        return n
    a,b = 1,2
    for i in range(3,n+1):
        c = b + (i-1)*a
        a = b
        b = c
    
    return c

print(friendPairFibo(4))