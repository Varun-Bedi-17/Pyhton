class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    
#  Recursive Method
    
# def height(root):
#     if root is None:
#         return 0
#     return 1 + max(height(root.left), height(root.right))

# def chck_balanced(root):
#     if root is None:
#         return True
#     lh = height(root.left)
#     rh = height(root.right)

#     if abs(lh-rh) <=1 and chck_balanced(root.left) and chck_balanced(root.right):
#         return True
#     return False

#--------------------------------------------------------------------------------------------------------------

def isBalanced(root):
    if root is None:
        return True, 0
    
    balance_l, height_l = isBalanced(root.left)
    balance_r, height_r = isBalanced(root.right)

    # if abs(height_l-height_r) <= 1 and balance_l and balance_r:
    #     return True, 1+max(height_l,height_r)
    # return False, 1+max(height_l,height_r)

    balanced = balance_l and balance_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height                                    # Less time taken





tree = Node(5)
tree.left = Node(2)
tree.right = Node(4)
tree.left.left = Node(7)
tree.right.left = Node(8)
tree.right.left.left = Node(9)
tree.right.left.right = Node(6)
tree.right.left.right.right = Node(1)


#               5
#             /   \
#           2       4
#          / \     /  \
#        7    None 8   None
#                 / \
#                9   6
#                     \
#                      1
# print(chck_balanced(tree))
balance,height = isBalanced(tree)
print(balance)



    #         1
    #       /   \
    #     2      3
    #   /  \
    # 4     5
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# print(chck_balanced(root))
balance,height = isBalanced(root)
print(balance)