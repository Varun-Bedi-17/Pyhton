class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Recursive Method  O(n**2)

# def height(root):
#     if root is None:
#         return 0
#     return 1 + max(height(root.left), height(root.right))

# def diameter(root):
#     if root is None:
#         return 0
#     left_h = height(root.left)
#     right_h = height(root.right)
#     # curr_dia = left_h + right_h +1

#     # left_d = diameter(root.left)
#     # right_d = diameter(root.right)

#     return max(left_h + right_h +1, max(diameter(root.left),diameter(root.right)))

# -------------------------------------------------------------------------------------------------------------
def diameter(root):
    ans = [0]
    def height(root,ans):
        if root is None:
            return 0

        left = height(root.left,ans)
        right = height(root.right,ans)

        ans[0] = max(ans[0], left+right+1)   # cuurent height = left+right+1
        return 1 + max(left, right)
    height(root,ans)
    return ans[0]

# for leetcode we need to find length therefore current height in both cases wil be = left + right




tree = Node(5)
tree.left = Node(2)
tree.right = Node(4)
tree.left.left = Node(7)
tree.right.left = Node(8)
tree.right.left.left = Node(9)
tree.right.left.right = Node(6)
tree.right.left.right.right = Node(1)



# print(tree.right.left.data)

#               5
#             /   \
#           2       4
#          / \     /  \
#        7    None 8   None
#                 / \
#                9   6
#                     \
#                      1

print(diameter(tree))


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

print(diameter(root))

