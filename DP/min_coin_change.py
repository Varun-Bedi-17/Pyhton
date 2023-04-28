# Minimum number of coins required
import sys

def coinChange(coins, amount):
    if amount == 0:
        return 0
    
    res = sys.maxsize

    for i in range(len(coins)):
        if coins[i] <= amount:
            answer = coinChange(coins, amount-coins[i])

            if answer != sys.maxsize and answer != -1:          # for below commented case
                res = min(res, answer+1)
    # print(res)

    return res if res != sys.maxsize else -1        #-1 for case coins = [2], amount = 3

# coins =[9,6,5,1]
# print(coinChange(coins, 11))



# -------------------------------------- DP


def CoinChangeDp(coins, V):
    table = [0 for i in range(V + 1)]
 
    table[0] = 0
 
    for i in range(1, V + 1):
        table[i] = sys.maxsize
 
        
    for i in range(1, V + 1):
        for j in range(len(coins)):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[i]):     #    if sub_res != sys.maxszie:
                    table[i] = sub_res + 1                                  #       table[i] = min(table[i], sub-res+1)
     
    if table[V] == sys.maxsize:
        return -1
       
    return table[V]

coins = [1, 2, 5]
print(CoinChangeDp(coins, 100))