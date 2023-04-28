def binary(arr, item):             # for descending order
    low, high = 0, len(arr)-1
    while low <=high:
        mid = (low + high)//2

        if arr[mid]==item:
            if mid-1 >= 0 and arr[mid-1] == item:          # check for repeated element
                high = mid-1
            else: 
                return mid
        
        elif arr[mid] < item:
            high = mid-1
        
        else:
            low = mid+1
    
    return -1

t1 = [13, 11, 10, 7, 4, 3, 1, 0]
t2 = [4, 2, 1, -1]             
t3 = [3, -1, -9, -127]
t4 = [6,6,6]
t5 = []
t6 = [9, 7, 5, 2, -9]
t7 = [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
t8 = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]

print(binary(t1, 7))
print(binary(t2, 4))
print(binary(t3, -127))
print(binary(t4, 6))
print(binary(t5, 7))
print(binary(t6, 4))
print(binary(t7, 3))
print(binary(t8, 6))
