def knap(values, weights, n, W):
    if n == 0 or W == 0:
        return 0
    
    elif weights[n-1] > W:
        return knap(values,weights, n-1, W)
    
    else:
        option1 = knap(values,weights,n-1,W-weights[n-1])+values[n-1]
        option2 = knap(values,weights, n-1, W)
        return max(option1, option2)

print(knap([100, 50, 150], [10, 20, 30], 3, 50))


## Memoization
def knap_memoization(capacity, weights, profits):
    memo = {}
    def knap_memo(capacity, i=0):
        key = (i,capacity)

        if key in memo:
            return memo[key]

        elif i==len(weights):
            memo[key] = 0

        elif weights[i] > capacity:
            memo[key] = knap_memo(capacity, i+1)

        else:
            memo[key] =  max(profits[i]+knap_memo(capacity-weights[i], i+1), knap_memo(capacity, i+1))
        
        return memo[key]
    return knap_memo(capacity)


print(knap_memoization(50, [10, 20, 30], [100, 50, 150]))



### DP
def knap_dp(capacity, weights, profits):
    n = len(weights)
    table = [[0 for i in range(capacity+1)] for j in range(n+1)]
    
    for i in range(n):
        for c in range(1,capacity+1):
            
            if weights[i] > c:
                table[i+1][c] = table[i][c]
                
            else:
                table[i+1][c] = max(profits[i]+table[i][c-weights[i]], table[i][c])
    return table[-1][-1]


print(knap_dp(50, [10, 20, 30], [100, 50, 150]))



