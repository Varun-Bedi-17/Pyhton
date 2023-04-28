
class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

tree = Node(5)
tree.left = Node(2)
tree.right = Node(4)
tree.left.left = Node(7)
tree.right.left = Node(8)


# print(tree.right.left.data)

#               5
#             /   \
#           2       4
#          / \     /  \
#        7    None 8   None