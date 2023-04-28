def quick(arr, start = 0, end =None):
    if end is None:
        end = len(arr)-1
    
    if start < end :
        pi = partition(arr, start, end)
        quick(arr,start,pi-1)
        quick(arr,pi+1,end)

def partition(arr, start, end):
    l, r = start, end-1

    while r>l:
        if arr[l] <= arr[end]:
            l += 1
        elif arr[r] > arr[end]:
            r -= 1
        else:
            arr[l],arr[r] = arr[r],arr[l]

    if arr[l] > arr[end]:
        arr[l],arr[end] = arr[end], arr[l]
        return l
    else:
        return end

    
array = [ 10, 7, 8, 9, 1, 5]
quick(array, 0, len(array) - 1)
print(array)

array2 = [64, 25, 12, 22, 11]
quick(array2)     
print(array2)

# Time Complexity = O(nlogn) and worst = O(n2)
# Auxiliary space = O(1)
# It is stable
