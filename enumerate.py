# enumerate(iterable, start = 0)  

# print(enumerate([1,5,3]))              #  <enumerate object at 0x0180CFA8>


# for x in enumerate([5,9,2]):
#     print(x)                           #  (0, 5) (1, 9) (2, 2)

for index,data in enumerate([5,9,2]):
    print(index, data)

print("")
############################################################################

l1 = ["afd", "oiu", "pre"]
s = "iyre"

print(*enumerate(l1))
for index,data in enumerate(l1):
    print(index,data)

print("")

for index,data in enumerate(s, 2):
    print(index,data)