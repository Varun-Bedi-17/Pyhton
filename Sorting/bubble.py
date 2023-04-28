def bubb(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
array = [64, 25, 12, 22, 11]
bubb(array)     
print(array)

# Time Complexity = O(n^2)-Worst,average and O(n)-Best case
# Auxiliary space = O(1)
# It is stable
# For best case, we can optimize this code by checking if inner loop does not make any swap.