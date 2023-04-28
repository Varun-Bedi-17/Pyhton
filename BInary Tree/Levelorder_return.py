class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Recursive Method - O(n**2)   and   O(n)

# def height(root):
#     if root is None:
#         return 0
#     return 1 + max(height(root.left), height(root.right))

# def CurrentLevel(root, level, lst):
#     if root is None:
#         return
#     if level == 1:
#         lst.append(root.data)
#     elif level>1:
#         CurrentLevel(root.left, level-1,lst)
#         CurrentLevel(root.right, level-1,lst)
#     return lst

# def LevelOrder(root):
#     h = height(root)
#     output = []
#     for i in range(1,h+1):
#         result = CurrentLevel(root,i, [])
#         output.append(result)
#     return output


#  Queue Method 

def level(root):
    q = []
    output = []
    q.append(root)

    while len(q) > 0:
        curr_level_size = len(q)
        level= []
        while curr_level_size > 0:
            node = q.pop(0)
            level.append(node.data)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            curr_level_size -= 1

        output.append(level)
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

order = level(tree)
print(order)