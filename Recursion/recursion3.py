##############                                     Reverse a String                      #######################

# def rev(s):
#     if len(s) == 0:
#         return
#     rev(s[1:])
#     print(s[0])

# rev("binod")

#  ---------------------------------------------------------------------------------------------------------

# def rev(s):
#     if len(s) == 0:
#         return s
#     return rev(s[1:]) + s[0]

# print(rev("binod"))




##########             Remove all duplicates from string                 ################

# def rem(s):
#     if len(s) == 1:
#         return s
#     ch = s[0]
#     ans = rem(s[1:])
#     if ch == ans[0]:
#         return ans
#     return ch+ans

# print(rem("aaaaaeeefffffffgaaaggggggb"))

# ---------------------------------------------------------------------------------------------------

# def rem(s):
#     if len(s) == 1 or len(s) == 0:
#         return s
#     if s[0] == s[1]:
#         return rem(s[1:])
#     return s[0] + rem(s[1:])

# print(rem("aaaaaaaaaaaaeeffffffffffgaaaaaaggggb"))




##################                Move all x to the end of string                    ###################

# def move(s,item):
#     if len(s) == 0:
#         return s
#     if s[0] == item:
#         return move(s[1:],item) + s[0]
#     return s[0] + move(s[1:],item)

# print(move("axxbdxcefxhix","x"))

# -----------------------------------------------------------------------------------------------------------

# def move(s,item):
#     if len(s) == 0:
#         return ""
#     ch = s[0]
#     ans = move(s[1:],item) 
#     if ch == item:
#         return ans+ch
#     return ch+ans

# print(move("axxbdxcefxhix","x"))




#############               Generate all substring from string                      ####################


# out = []
# def subs(s,ans):
#     if len(s) == 0:
#         out.append(ans)
#         return ""

#     ch = s[0]
#     subs(s[1:],ans) 
#     subs(s[1:],ans+ch)  
#     return out

# print(subs("ABC", ""))