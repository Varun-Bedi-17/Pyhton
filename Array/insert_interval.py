def insert(lists, new):
        s, e = new[0], new[1]
        left, right = [], []
        for i in lists:
            if i[1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[1])

        return left + [list((s,e))] + right

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

