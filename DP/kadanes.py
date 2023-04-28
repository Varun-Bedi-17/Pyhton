#    -------------------   Kadane's algorithm -> Sum of contigous sub-array    ------------------------------
import sys


def kadane(arr):
    curr = 0
    maxTillnow = -sys.maxsize -1
    for i in range(len(arr)):
        curr += arr[i]
        maxTillnow = max(curr, maxTillnow)

        if curr < 0:
            curr = 0

    return maxTillnow

# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# a1 = [-5, -1, 5, -3, -1, 2, 3, -6]
# print(kadane(a1))


# -------------------------- Print start and end index of max subarray --------------------------

def kadane_print(arr):
    curr, start, end, s = 0, 0, 0, 0
    maxTillnow = -sys.maxsize -1
    for i in range(len(arr)):
        curr += arr[i]
        # maxTillnow = max(curr, maxTillnow)
        
        if maxTillnow < curr:
            maxTillnow = curr
            end = i
            start =s               # For single term

        if curr < 0:
            curr = 0
            s = i+1

    return maxTillnow,start,end


a = [-2, -3, 4, -1, -2, 1, 5, -3]
a1 = [-5, -1, 5, -3, -1, 2, 3, -6]
a3 = [-1,-2,5,-2,5]
a4 = [-1]
print(kadane_print(a3))


# -------------------------------- Another method(Divide and conquer)---------------------------