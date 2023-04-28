class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def left_view(root):
    if root is None:
        return []
    q = []
    output = []
    q.append(root)

    while len(q) > 0:
        curr_level_size = len(q)
        for i in range(curr_level_size):
            node = q.pop(0)

            if i == 0:
                output.append(node.data)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    return output


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
print(left_view(tree))





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

print(left_view(root))