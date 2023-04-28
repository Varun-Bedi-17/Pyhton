###########                  Find first and last ocuurence of an item in an array                ################


# def firstocc(l,i,item):
#     if i ==len(l):
#         return -1
#     if l[i] == item:
#         return i
#     return firstocc(l,i+1,item)

# print(firstocc([4,2,3,5,7,2,1,2,9],0,2))


# def lastocc(l,i,item):
#     if i ==len(l):
#         return -1
#     occ = lastocc(l,i+1,item)
#     if l[i] == item and occ ==-1:
#         occ = i
#     return occ

# print(lastocc([4,2,3,5,7,2,1,2,3,2,9],0,2))