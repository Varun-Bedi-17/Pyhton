def knap(values, weights, n, W):
    if n == 0:
        return (W//weights[0])*values[0]
    
    option1 = knap(values,weights, n-1, W)
    option2 = -1

    if weights[n] <= W:
        option2 = knap(values,weights,n,W-weights[n])+values[n]

    return max(option1, option2)

print(knap([10, 30, 20, 70], [5, 10, 15, 20], 3, 100))   # 3 = len-1



# --------------------------------------- DP
def unboundedKnapsack(values, weights, n, W):
    dp = [0 for i in range(W + 1)]
 
    for i in range(W + 1):
        for j in range(n):
            if (weights[j] <= i):
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])

    return dp[W]

N = 4
print(unboundedKnapsack([10, 30, 20, 70], [5, 10, 15, 20], N, 100))
