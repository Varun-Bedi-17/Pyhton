l1 = [[1,2,3], [8,9,0]]
l2 = [[4,5,6], [7,53,78]]

print(list(zip(l1,l2)))              #   [([1, 2, 3], [4, 5, 6]), ([8, 9, 0], [7, 53, 78])]

for i,(l1_item,l2_item) in enumerate(zip(l1, l2)):
    print(i, list(zip(l1_item, l2_item)))


for l1_item,l2_item in zip(l1, l2):
    print(list(zip(l1_item, l2_item)))



# Make two lists from list of lists
l = [[2,3], [7,8], [5,6]]

l1, l2 = zip(*l)
print(l1)
print(l2)