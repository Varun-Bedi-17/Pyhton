# from itertools import combinations

# l = [1,1]
# l.sort()
# output = []
# result = []
# target = 2

# if len(l) == 1 and l[0] == target:
#     result.append([l[0]])
#     print(l)

# for i in range(1,len(l)+1):
#     output+= list(combinations(l,i))

# output = list(set(output))

# for item in output:
#     if sum(item)==target:
#         result.append(item)

# print(result)                           # Space complexity is too much .




# --------------------------------------------- Backtracking

def combinationSum2(candidates, target):
        def recurse(index, target, output, result):
            if target == 0:
                result.append(list(output))
                return
                
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:         # To remove similar groups
                    continue

                if target-candidates[i] >= 0:
                    output.append(candidates[i])
                    
                    recurse(i+1, target-candidates[i], output, result)
                    
                    output.remove(candidates[i])
        
        
        
        candidates.sort()
        output = []
        result = []
        
        recurse(0, target, output, result)
        return result

print(combinationSum2([10,1,2,7,6,1,5], 8))