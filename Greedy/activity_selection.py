# Also useful in leetcode-452 problem

def activitySelection(arr):
    answer = []
    arr.sort(key = lambda x: x[1])       # arr.sort(key = operator.itemgetter(1))     import operator
                                         # itemgetter mmust be use in case list cotains only digits
    i = 0
    answer.append(arr[i])

    for j in range(1, len(arr)):
        if arr[j][0] >= arr[i][1]:
            answer.append(arr[j])
            i = j

    return answer

Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
# print(activitySelection(Activity))





# --------------  When we need to find the no of selections

def activitySelectionCount(arr):
    arr.sort(key = lambda x: x[1])

    take = 1
    activity_taken = arr[0][1]

    for j in range(1, len(arr)):
        if arr[j][0] >= activity_taken:
            take += 1
            activity_taken = arr[j][1]

    return take

Activity = [[7,8],[2,4],[2,7],[3,10]]
# print(activitySelectionCount(Activity))



# ------------------------------ When two array start and end is given

def activitySelection_two(n,start,end):
        arr = [(item1,item2) for item1, item2 in zip(start, end)]
        arr.sort(key = lambda x: x[1])
        

        take = 1
        activity_taken = arr[0][1]
    
        for j in range(1, n):
            if arr[j][0] > activity_taken:          # We have two only greater than case
                take += 1
                activity_taken = arr[j][1]
    
        return take

N = 4
start = [1, 3, 2, 5]
end = [2, 4, 3, 6]
print(activitySelection_two(N, start, end))