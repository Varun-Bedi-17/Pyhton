# ------------------------------------  Recursive

def lis(prev, curr, arr, n):
    if curr == n:
        return 0

    x = lis(prev, curr+1, arr, n)   # Do not take
    y = 0

    if arr[prev] < arr[curr] or prev == -1:             # when we take element
        y = 1 + lis(curr, curr+1,arr, n)

    return max(x,y)



numbers = [10,9,2,5,3,7,101,18]
N = len(numbers)

# print(lis(-1, 0, numbers, N))



# ------------------------------------- Memoization

def lis_memo(prev, curr, arr, n):

    def recurse(prev, curr):
        if curr == n:
            return 0

        key = (prev, curr)

        if key in memo:
            return memo[key]

        x = recurse(prev, curr+1)   # Do not take
        y = 0

        if arr[prev] < arr[curr] or prev == -1:             # when we take element
            y = 1 + recurse(curr, curr+1)

        memo[key] = max(x,y)
        return memo[key]

    memo = {}
    return recurse(-1, 0)


# numbers = [10,9,2,5,3,7,101,18]
# N = len(numbers)
# numbers2 = [0,1,0,3,2,3]
# print(lis_memo(-1,0,numbers2,len(numbers2)))

# We can create table[prev][current] but then space complexity we O(n2)

# ------------------------------------- DP
def lengthOfLIS(arr):
        n = len(arr)
 
        lis = [1]*n

        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j]:
                    lis[i] = max(lis[i], lis[j]+1)
            print(lis)

        maximum = 0

        for i in range(n):
            maximum = max(maximum, lis[i])

        return maximum
 

numbers = [10,9,2,5,3,7,101,18]
numbers2 = [0,1,0,3,2,3]
print(lengthOfLIS(numbers))



 