################                 Check if an array is sorted or not                      #################


# def chckArray(l):
#     if len(l) == 1:
#         return True
#     if l[0] > l[1]:
#         return False
#     return chckArray(l[1:])

# print(chckArray([1,1,2,3,2,5,6]))

# ---------------------------------------------------------------------------------------------------------------

# def chckArray(l):
#     if len(l) == 1:
#         return True
#     rec = chckArray(l[1:])
#     # if l[0]<= l[1] and rec:
#     #     return True
#     # else:
#     #     return False
#     return l[0] <= l[1] and rec

# print(chckArray([1,1,2,3,2,5,6]))




###############               Print numbers till n in dec order                  ###################

# def dec(n):
#     if n==0:
#         return
#     print(n)
#     return dec(n-1)

# dec(5)




###############               Print numbers till n in inc order                  ###################

# def inc(n):
#     if n==0:
#         return
#     inc(n-1)
#     print(n)

# inc(6)