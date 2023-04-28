import sys
def McM(start, end, arr):
    if start >= end:
        return 0

    ans= sys.maxsize
    for i in range(start, end):
        count = McM(start, i, arr) + McM(i+1, end, arr) + (arr[start-1] * arr[i] * arr[end])

        if count < ans:
            ans = count

    return ans


arr = [1, 2, 3, 4, 3]
print(McM(1, len(arr)-1, arr))




# ----------------------------------- Memoization

def McM_memo(start, end, arr):
    def recurse(start, end):
        if start >= end:
            return 0

        key = (start,end)

        if key in memo:
            return memo[key]

        ans= sys.maxsize
        for i in range(start, end):
            count = recurse(start, i) + recurse(i+1, end) + (arr[start-1] * arr[i] * arr[end])

            if count < ans:
                ans = count
                memo[key] = count

        return memo[key]

    memo = {}
    return recurse(start, end)


arr = [1, 2, 3, 4, 3]
# print(McM_memo(1, len(arr)-1, arr))



# ---------------------------------------- DP
