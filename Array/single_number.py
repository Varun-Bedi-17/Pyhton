#    --------------------------- Basic Approach [O(n2) and O(1)]
def singleNumber(nums):
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            check = 0
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j]:
                        check += 1
                        break
            if check == 0:
                return nums[i]
        return nums[len(nums)-1]

arr = [2, 4, 6, 2, 4, 9, 7, 6, 9]
# print(singleNumber(arr))




# -------------------------------------------- Using Sorting [O(nlogn) and O(1)]
def singleNumberSort(nums):
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[-1]

# print(singleNumberSort(arr))




# ----------------------------------------- Using dictionary [O(n) and O(n)]

def singleNumberDict(nums):
        d = {}
        for item in nums:
            if item in d:
                d.pop(item)                # del d[items]
            else:
                d[item] = 1
        return list(d.keys())[0]

# print(singleNumberDict(arr))




# ------------------------------------------- Using Bit Manupulation[ O(n) and O(1) ]

def singleNumberBM(nums):
        ans =0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
            # print(ans)
        return ans

print(singleNumberBM(arr))