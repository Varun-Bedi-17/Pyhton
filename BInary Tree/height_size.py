class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

# Sum of all nodes
def sum_nodes(root):
    if root is None:
        return 0
    return  root.data + sum_nodes(root.left) + sum_nodes(root.right)

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

print(height(tree))
print(size(tree))
print(sum_nodes(tree))