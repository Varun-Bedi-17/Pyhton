# Sort list of lists according to first element of list
from operator import itemgetter

lists = [[60,30], [100,20], [120,10], [150,50]]
# -------------------------------------- Using Sort -------------------------------------------

lists.sort(key=lambda x: x[1])
print(lists)

# lists.sort(key=itemgetter(1))                  # Itemgetter method
# print(lists)


# -------------------------------------- Using Sorted -------------------------------------------
# lists = sorted(lists, key= lambda x: x[1])
# print(lists)

# print(sorted(lists, key= itemgetter(1)))



# ------------------------------ Reverse(In descending order)  ------------------------------
lists.sort(key=lambda x: x[1], reverse=True)
print(lists)