# No. of ways we can make value(V) by using coins.  This problem is coin change(ii).

def coinChange(arr, n, V):
    if V == 0:
        return 1

    if V < 0:
        return 0

    if n <=0:
        return 0

    take_coin = coinChange(arr, n, V-arr[n-1])
    do_not_take = coinChange(arr, n-1, V)
    return take_coin + do_not_take


# print(coinChange([1,2,3], 3, 6))



# --------------------------------------   Memoization

def coin_memo(arr, n, V):
    def recurse(n,V):

        key = (n,V)

        if V == 0:
            return 1

        if V < 0:
            return 0

        if n <=0:
            return 0

        if key in d:
            return d[key]

        take_coin = recurse(n, V-arr[n-1])
        do_not_take = recurse(n-1, V)
        d[key] = take_coin + do_not_take

        return d[key]

    d = {}
    return recurse(n, V)


# print(coin_memo([1,2,3], 3, 6))
# print(coin_memo([1,2], 2, 4))



# ---------------------------------------   DP
#  Use the table in register

def coin_dp(arr, n, V):
    table = [[0 for i in range(V+1)] for j in range(n)]

    for i in range(n):      # Make first columns of 0
        table[i][0] = 1
    

    for i in range(n):
        for j in range(1,V+1):      # as we already make 0th element of all columns 1, so we start with 2nd column(index=1)

            if j-arr[i] >= 0:
                x = table[i][j - arr[i]]          
            else:
                x = 0

            y = table[i-1][j]        # Upward element
 
            table[i][j] = x + y

        print(table)

    return table[-1][-1]

print(coin_dp([1,2], 2, 6))



