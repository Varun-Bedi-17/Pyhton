def insertion_sort(nums):
    for i in range(1,len(nums)):
        cur = nums.pop(i)    # we have to pop element mandatorily as we insert element at this position below.
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
        

array = [64, 25, 12, 22, 11]
insertion_sort(array)
print(array)



def insert(arr):
    for i in range(1, len(arr)):
        key = arr[i]        # we need to use this mandatorily as we change the position of elements below
  
        j = i-1
        while j >= 0 and key < arr[j]:# if we use arr[i] here and below in place of key then ouput is [64, 64, 64, 64, 64]
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

array2 = [64, 25, 12, 22, 11]
insert(array2)
print(array2)


# Time Complexity = O(n^2)-Worst,average and O(n)-Best case
# Auxiliary space = O(1)
# It is stable