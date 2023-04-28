def selection(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in  range(i+1,n):
            if arr[j] < arr[min_idx]:           # For decreasing order we change `<` to `>`.
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
    


array = [64, 25, 12, 22, 11]
selection(array)            ## Python always pass by reference
print(array)

# Time Complexity = O(n^2)
# Auxiliary space = O(1)

# A sorting algorithm is said to be stable if two objects
# with equal or same keys appear in the same order in sorted output as they appear in the input array to be sorted.

# Selection sort is not stable.
