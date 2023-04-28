#  Leetcode-56

def chck(lists):
    i = 0
    count = 0
    lists.sort(key=lambda x:x[0])
    n = len(lists)

    if n == 1:
        return lists

    while count < n and i+1 < len(lists):
        if lists[i][1] >= lists[i+1][0] or lists[i][0]>= lists[i+1][0]:
            lists[i][0] = min(lists[i][0], lists[i+1][0])
            lists[i][1] = max(lists[i][1], lists[i+1][1])
            lists.pop(i+1)
        else:
            i += 1
        count +=1
    return lists

print(chck([[2,3],[4,5],[6,7],[8,9],[1,10]]))
