##    Using linear Search
def count_rotations_linear(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i+1
    return 0

print(count_rotations_linear([5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]))


## Using binary search

def binary(nums):              # for ascending and sorted array
    lo, hi = 0, len(nums)-1

    while lo<=hi:
        mid = (lo+hi)//2
        if mid+1 < len(nums) and nums[mid] > nums[mid+1]:
            return mid+1
        
        elif nums[mid] < nums[hi]:
            hi = mid - 1

        else:
            lo = mid+1

    return 0

print(binary([0, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 8, 8, 9, 9, 9, 9]))
