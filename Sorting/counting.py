def counting_sort(arr):
    max_ele = max(arr)
    size = len(arr)

    count = [0] * (max_ele+1)
    output = [0]*size

    for item in arr:
        count[item] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    i = size-1
    while i >= 0:
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    return output

data = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(data))

array = [64, 25, 12, 22, 11]
print(counting_sort(array))

array2 = [12, 11, 13, 5, 6, 7]
print(counting_sort(array2))

# Time Complexity = O(n+k) in all cases. n = input, k = max_ele
# Auxiliary space = O(k)
# It is stable

# arr = [-5, -10, 0, -3, 8, 5, -1, 10]          # This method doesn't work with negative numbers
# print(counting_sort(arr))




#                 Program for negattive numbers also                         

def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1

    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 

    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 

    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    return output_arr
 
 
arr = [-5, -10, 0, -3, 8, 5, -1, 10]
ans = count_sort(arr)
print(ans)

# data = [4, 2, 2, 8, 3, 3, 1]
# print(counting_sort(data))

# array = [64, 25, 12, 22, 11]
# print(counting_sort(array))

# array2 = [12, 11, 13, 5, 6, 7]
# print(counting_sort(array2))