# output = []
# def perm(s, ans):
#     if len(s) == 0:
#         output.append(ans)
#         return

#     # ch = s[0]
#     for i in range(len(s)):
#         ch = s[i]
#         perm(s[0:i]+s[i+1:],ans+ch)

#     return output

# print(perm("ABC",""))