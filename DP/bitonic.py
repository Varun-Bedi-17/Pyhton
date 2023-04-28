# ---- Bitonic Sequence- either increasing or either decreasing or either increasing and then decreasing -----

def longestBitonic(arr):
    n = len(arr)
    increasing_sub = [1 for _ in range(len(arr)+1)]
    deccreasing_sub = [1 for _ in range(len(arr)+1)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                increasing_sub[i] = max(increasing_sub[i], increasing_sub[j]+1)


    for i in range(n-2, -1, -1):                # For lomgest decreasing sub
        for j in range(n-1, i, -1):
            if arr[i] > arr[j]:
                deccreasing_sub[i] = max(deccreasing_sub[i], deccreasing_sub[j]+1)

    maximum = 0
    for i in range(n):
        maximum = max(maximum, increasing_sub[i]+deccreasing_sub[i]-1)

    
    return maximum


arr =  [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]
arr2= [1, 11, 2, 10, 4, 5, 2, 1]
print(longestBitonic(arr2))

    