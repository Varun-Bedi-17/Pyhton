# ---------------------------------------- Recursive

def oGame(i, j, arr):

    if i == j:
        return arr[i]
    
    if i > j:                      # if j < 0 or i>=len(arr) or i > j = Only one line for thesetwo if conditions.
        return 0

    option1 = arr[i] + min(oGame(i+2, j, arr), oGame(i+1, j-1, arr))
    option2 = arr[j] + min(oGame(i+1, j-1, arr), oGame(i, j-2,arr))

    return max(option1, option2)


# arr1 = [8, 15, 3, 7]
# print(oGame(0, len(arr1)-1, arr1)) 

# arr2 = [2, 2, 2, 2]
# print(oGame(0, len(arr2)-1, arr2))
 
# arr3 = [20, 30, 2, 2, 2, 10]
# print(oGame(0, len(arr3)-1, arr3))




# ---------------------------------------- Memoization

def oGame_memo(i, j, arr):
    def recur(i,j):
    
        if j < 0 or i>=len(arr) or i > j:
            return 0

        key = (i,j)
        if key in memo:
            return memo[key]

        option1 = arr[i] + min(recur(i+2, j), recur(i+1, j-1))
        option2 = arr[j] + min(recur(i+1, j-1), recur(i, j-2))

        memo[key] = max(option1, option2)
        return memo[key]

    memo = {}
    return recur(i,j)


# arr1 = [8, 15, 3, 7]
# print(oGame_memo(0, len(arr1)-1, arr1)) 

# arr2 = [2, 2, 2, 2]
# print(oGame_memo(0, len(arr2)-1, arr2))
 
# arr3 = [20, 30, 2, 2, 2, 10]
# print(oGame_memo(0, len(arr3)-1, arr3))



# -------------------------------- DP

def game_dp(arr):
    n = len(arr)
    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i,n):
            k = j-i

            x = 0
            if k+2 <=j:
                x = table[k+2][j]

            y = 0
            if k+1 <= j-1:
                y = table[k+1][j-1]

            z = 0
            if k <= j-2:
                z = table[k][j-2]

            option1 = arr[i] + min(x,y)
            option2 = arr[j] + min(y,z)

            table[k][j] = max(option1, option2)

    print(table)
    return table[0][n-1]



# arr1 = [8, 15, 3, 7]
# print(game_dp(arr1)) 

# arr2 = [2, 2, 2, 2]
# print(game_dp(arr2))
 
# arr3 = [20, 30, 2, 2, 2, 10]
# print(game_dp(arr3))

