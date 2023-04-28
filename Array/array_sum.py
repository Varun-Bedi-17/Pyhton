def combinationSum(candidates, target):
    def recursive(index, target, output, result):
        if target == 0:
            result.append(list(output))
            return

        for i in range(index, len(candidates)):
            if target-candidates[i] >= 0:
                output.append(candidates[i])

                recursive(i, target-candidates[i], output, result)

                output.pop()                    # Backtracking    output.remove(candidates[i])


    result = []
    output = []
    recursive(0, target, output, result)
    return result


print(combinationSum([2,3,6,7], 7))
