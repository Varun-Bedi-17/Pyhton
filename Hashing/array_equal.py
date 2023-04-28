# Minimum change to make all elements of array equal

def minOperation(arr):
    d= {}
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]]+=1
        else:    
            d[arr[i]] = 1

    max_count = 0
    for i in d:
        if max_count < d[i]:
            max_count = d[i]
    
    return len(arr) - max_count



arr = [1, 5, 2, 1, 3, 2, 1]
n = len(arr)
print(minOperation(arr))

