# ------------------------------------- Recursive
def minJumps(arr, l, n):
 
    if (n == l):
        return 0
 
    if (arr[l] == 0):
        return float('inf')
 
    min = float('inf')
    for i in range(l + 1, n + 1):
        if (i <= l + arr[l]):
            jumps = minJumps(arr, i, n)
            if (jumps != float('inf') and
                    jumps + 1 < min):
                min = jumps + 1
 
    return min
 
 
arr = [2,3,0,1,4]
n = len(arr)
# print(minJumps(arr, 0, n-1))




# --------------------------------------- DP

import sys
def min_jump_dp(arr):
    N = len(arr)
    dp = [0 for _ in range(N)]

    if N == 0 or arr[0] == 0:
        return -1

    for i in range(1,N):
        dp[i] = sys.maxsize
        for j in range(i):
            if i <= j+arr[j]:
                dp[i] = min(dp[i], dp[j]+1)

    return dp[-1]


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# print(min_jump_dp(arr))



# ----------------------------------------- Greedy Approach

def min_jump_greedy(arr):
    N = len(arr)

    if N <=1 or arr[0] == 0:
        return 0

    maxReach = arr[0]
    step = arr[0]

    jumps = 1

    for i in range(1, N):
        if i == N-1:
            return jumps

        maxReach = max(maxReach, i+arr[i])

        step -= 1

        if step == 0:
            jumps += 1

            if(i >= maxReach):         # for case: [1,0,3]
                return -1

            step = maxReach - i
            

    return -1


arr = [2,3,0,1,4]
print(min_jump_greedy(arr))