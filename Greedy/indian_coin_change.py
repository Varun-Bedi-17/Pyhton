def ICoinChange(value):
    count = 0

    i = len(coins)-1
    while i >= 0:             # value > 0:
        count += value//coins[i]
        value = value - (value//coins[i] * (coins[i]))
        i -= 1
    
    return count


coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
print(ICoinChange(1028))

# But this approach is wrong for other values of coins like [9, 6, 5, 1] , Expected Answer =2, Output = 3.
# Therefore, for different values of coins we need to use recursion and dp.