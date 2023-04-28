class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def sumroot(root):
    if root is None:
        return
    sumroot(root.left)
    sumroot(root.right)

    if root.left is not None:
        root.data += root.left.data
    if root.right is not None:
        root.data +=root.right.data





tree = Node(5)
tree.left = Node(2)
tree.right = Node(4)
tree.left.left = Node(7)
tree.right.left = Node(8)
tree.right.left.left = Node(9)
tree.right.left.right = Node(6)
tree.right.left.right.right = Node(1)

sumroot(tree)
print(tree.data)  # 42
print(tree.left.data)  # 9
print(tree.right.data)  # 28
print(tree.left.left.data)  # 7
print(tree.right.left.data)  # 24
print(tree.right.left.right.data)  # 7




#               5
#             /   \
#           2       4
#          / \     /  \
#        7    None 8   None
#                 / \
#                9   6
#                     \
#                      1


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