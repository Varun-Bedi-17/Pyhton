def merge_sort(nums):

    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    
    left = nums[:mid]
    right = nums[mid:]
    
    # Solve the problem for each half recursively
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Combine the results of the two halves
    sorted_nums =  merge(left_sorted, right_sorted)
    
    return sorted_nums

def merge(left, right):
    merged = []

    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        
    return merged + left[i:] +right[j:]



array = [64, 25, 12, 22, 11]
print(merge_sort(array))

array2 = [12, 11, 13, 5, 6, 7]
print(merge_sort(array2))