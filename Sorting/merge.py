def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2

        Left = arr[ :mid]
        Right = arr[mid:]
        
        merge_sort(Left)
        merge_sort(Right)

        i,j,k = 0,0,0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                k += 1
                i += 1

            else:
                arr[k] = Right[j]
                k += 1
                j += 1

        while i < len(Left):
            arr[k] = Left[i]
            k += 1
            i += 1
        
        while j < len(Right):
            arr[k] = Right[j]
            k += 1
            j += 1





array = [64, 25, 12, 22, 11]
merge_sort(array)
print(array)

array2 = [12, 11, 13, 5, 6, 7]
merge_sort(array2)
print(array2)

# Time Complexity = O(nlogn)
# Auxiliary space = O(n)
# It is stable

