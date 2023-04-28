def linear(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

t1 = [13, 11, 10, 7, 4, 3, 1, 0]
t2 = [2, 1, -1, 4]              # Also works in unsorted
t3 = [3, -1, -9, -127]
t4 = [6]
t5 = []
t6 = [9, 7, 5, 2, -9]
t7 = [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
t8 = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]

print(linear(t1, 7))
print(linear(t2, 4))
print(linear(t3, -127))
print(linear(t4, 6))
print(linear(t5, 7))
print(linear(t6, 4))
print(linear(t7, 3))
print(linear(t8, 6))