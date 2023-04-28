def counting(arr, divisor):
    output = [0]* len(arr)
    count = [0]*10           # Because single digit is always from 1 to 9

    for i in range(len(arr)):
        index = arr[i] // divisor
        count[index % 10] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    i = len(arr) - 1
    while i >= 0:
        ind = arr[i] // divisor
        output[count[ind %10]-1] = arr[i]
        count[ind %10] -= 1
        i -= 1

    for j in range(len(output)):
        arr[j] = output[j]


def radix_sort(arr):
    maximum = max(arr)

    divisor = 1
    while maximum // divisor >= 1:
        counting(arr, divisor)
        divisor = divisor*10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)
    
data = [4, 2, 2, 8, 3, 3, 1]
radix_sort(data)
print(data)

array = [64, 25, 12, 22, 11]
radix_sort(array)
print(array)

array2 = [12, 11, 13, 5, 6, 7]
radix_sort(array2)
print(array2)

 # Time Complexity = O(dn) in all cases where d = number of digits in largest number
# Auxiliary space = O(n+k) n = size of array, k = largest element among dth place elements(ones, tens, hundreds etc)
# It is stable