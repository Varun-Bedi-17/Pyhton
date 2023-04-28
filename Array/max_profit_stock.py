# ----------------------------------------------Leetcode -121 
# ----------------------------------------------Basic Approach [ O(n2) and O(1)]

def maxProfit(prices):
    if sorted(prices, reverse=True) == prices:
        return 0

    ans = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            # if prices[j] > prices[i]:
            ans = max(ans, prices[j]-prices[i])

    return ans



l = [7,1,5,3,6,4]
# print(maxProfit(l))




# ---------------------------------- [O(n) and O(n)]  (Anuj Bhaiya)
def maxProfitA(prices):
    n = len(prices)
    ans = 0

    maxSoFar = [0 for _ in range(n)]
    maxSoFar[n-1] = prices[n-1]

    for i in range(n-2,-1,-1):
        maxSoFar[i] = max(prices[i], maxSoFar[i+1])

    for i in range(n):
        ans = max(ans, maxSoFar[i]-prices[i])

    return ans


l = [7,1,5,3,6,4]
print(maxProfitA(l))






# --------------------------------------- Greedy Approach[O(n) and O(1)]
def maxProfitGreedy(prices):
    buy = prices[0]
    ans = 0

    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]

        elif prices[i] - buy > ans:
            ans = prices[i]- buy
    
    return ans

l = [2,4,1]
# print(maxProfitGreedy(l))