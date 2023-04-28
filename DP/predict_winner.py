# ---------------------------------------- Recursive

def PredictTheWinner(nums):
        def oGame(i, j, arr):

            if i == j:
                return arr[i]

            if i > j:                     
                return 0

            option1 = arr[i] + min(oGame(i+2, j, arr), oGame(i+1, j-1, arr))
            option2 = arr[j] + min(oGame(i+1, j-1, arr), oGame(i, j-2,arr))

            return max(option1, option2)
            
        sum_1 = oGame(0, len(nums)-1, nums)
        sum_2 = sum(nums) - sum_1
        
        return sum_1 >= sum_2

# arr = [1, 5, 2]
# print(PredictTheWinner(arr))

# arr1 = [8, 15, 3, 7]
# print(PredictTheWinner(arr1))
 
# arr3 = [949829,1462205,1862548,20538,8366111,5424892,7189089,9,5301221,5462245,0,2,4,9401420,4937008,1,9,7,4146539]
# print(PredictTheWinner(arr3))




# ------------------------------------ Memoization
def PredictTheWinner_memo(nums):
        def oGame(i, j):

            if i == j:
                return nums[i]

            if i > j:                     
                return 0
            key = (i,j)
            if key in memo:
                return memo[key]

            option1 = nums[i] + min(oGame(i+2, j), oGame(i+1, j-1))
            option2 = nums[j] + min(oGame(i+1, j-1), oGame(i, j-2))

            memo[key] = max(option1, option2)
            return memo[key]
        
        memo = {}    
        sum_1 = oGame(0, len(nums)-1)
        sum_2 = sum(nums) - sum_1
        
        return sum_1 >= sum_2


# arr = [1, 5, 2]
# print(PredictTheWinner_memo(arr))

# arr1 = [8, 15, 3, 7]
# print(PredictTheWinner_memo(arr1))
 
# arr3 = [949829,1462205,1862548,20538,8366111,5424892,7189089,9,5301221,5462245,0,2,4,9401420,4937008,1,9,7,4146539]
# print(PredictTheWinner_memo(arr3))


# ---------------------------------- Another basic approach
def PredictTheWinner_ab(nums):
        def pred(i, j, target):
            if i == j:
                return target*nums[i]
            
            option1 = target *nums[i] + pred(i+1, j, -target)
            option2 = target *nums[j] + pred(i,j-1, -target)
            
            return target * max(target*option1, target*option2)
        return pred(0, len(nums)-1, 1) >=0

# arr = [1, 5, 2]
# print(PredictTheWinner_ab(arr))

# arr1 = [8, 15, 3, 7]
# print(PredictTheWinner_ab(arr1))
 
# arr3 = [949829,1462205,1862548,20538,8366111,5424892,7189089,9,5301221,5462245,0,2,4,9401420,4937008,1,9,7,4146539]
# print(PredictTheWinner_ab(arr3))

# Time Complexity = O(2^n)




# ---------------------------- Another approach memo
def PredictTheWinner_ab_memo(nums):
        def pred(i, j, target):
            if i == j:
                return target*nums[i]

            key = (i,j)
            if key in memo:
                return memo[key]
            
            option1 = target *nums[i] + pred(i+1, j, -target)
            option2 = target *nums[j] + pred(i,j-1, -target)
            
            memo[key] = target * max(target*option1, target*option2)
            return memo[key]
        
        memo = {}
        return pred(0, len(nums)-1, 1) >=0


# arr = [1, 5, 2]
# print(PredictTheWinner_ab_memo(arr))

# arr1 = [8, 15, 3, 7]
# print(PredictTheWinner_ab_memo(arr1))
 
# arr3 = [949829,1462205,1862548,20538,8366111,5424892,7189089,9,5301221,5462245,0,2,4,9401420,4937008,1,9,7,4146539]
# print(PredictTheWinner_ab_memo(arr3))



# We can omit the use of target ny subtracting score of player1 from player2 in each iteration.

def prediction(arr):
    def recurse(i,j):
        if i==j:
            return arr[i]
        
        key = (i,j)
        
        if key in memo:
            return memo[key]

        option1 = arr[i] - recurse(i+1,j)
        option2 = arr[j] - recurse(i, j-1)

        memo[key] =  max(option1, option2)
        return memo[key]
    
    memo = {}
    return recurse(0, len(arr)-1) >= 0

arr = [1, 5, 2]
print(prediction(arr))

arr1 = [8, 15, 3, 7]
print(prediction(arr1))
 
arr3 = [949829,1462205,1862548,20538,8366111,5424892,7189089,9,5301221,5462245,0,2,4,9401420,4937008,1,9,7,4146539]
print(prediction(arr3))