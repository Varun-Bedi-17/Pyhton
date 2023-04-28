#   Using Linear Search              Works For repeated elements also

def search(nums, item):
    for i in range(len(nums)):
        if nums[i] == item:
            return i

    return -1

def searchWhile(nums, target):
    position = 0
    
    while position < len(nums):
        if nums[position] == target:
            return position
        position += 1
    return -1


#  Binary Search     Not work for repeated elements
def search1Binary(nums, target):    
    lo = 0
    hi = len(nums)-1
    
    while lo<=hi:
        mid = (lo + hi) // 2
        
        if nums[mid] == target:
            if mid-1 >= 0 and nums[mid-1] == target:          # check for repeated element
                hi = mid-1
            else: 
                return mid

        elif ((nums[lo] == nums[mid]) and (nums[hi] == nums[mid])) :    # for tricky case [1,0,1,1,1], 0
            lo += 1
            hi -= 1

        elif nums[lo] <= nums[mid]:
            # left half is sorted
            if nums[lo] <= target and target <= nums[mid]:
                hi = mid -1
            else:
                lo = mid+1
              
        
        else:
            #the right half is sorted
            if nums[mid] <= target and target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid-1
    
    return -1

print(search([4,5,6,7,0,1,2], 6))
print(searchWhile([4,5,6,7,0,1,2], 6))
print(search1Binary([4,5,6,7,0,1,2], 6))
print(search1Binary([1,0,1,1,1], 0))


print(search([0, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 8, 8, 9, 9, 9, 9], 6))
print(searchWhile([0, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 8, 8, 9, 9, 9, 9], 6))
print(search1Binary([0, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 8, 8, 9, 9, 9, 9], 6))