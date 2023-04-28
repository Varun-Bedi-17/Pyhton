l = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

# def phn(digits,ans):
#     if len(digits) == 0:
#         print(ans,end=" ")
#         return ""

#     n = l[int(digits[0])]
#     for i in range(len(n)):
#         phn(digits[1:], ans+n[i])

# print(phn("23",""))

# -------------------------------------------------------------------------------------------


# output = []
# comb = []
# def phn(digits):
#     if len(digits) == 0:
#         comb.append("".join(output))
#         return

#     n = l[int(digits[0])]
#     for i in range(len(n)):
#         output.append(n[i])
#         phn(digits[1:])
#         output.pop()
#     return comb

# print(phn("23"))