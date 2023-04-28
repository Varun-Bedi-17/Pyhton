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

# def CurrentLevel(root, level):
#     if root is None:
#         return
#     if level == 1:
#         print(root.data,end=" ")
#     elif level>1:
#         CurrentLevel(root.left, level-1)
#         CurrentLevel(root.right, level-1)

# def LevelOrder(root):
#     h = height(root)
#     for i in range(1,h+1):
#         CurrentLevel(root,i)


# ---------------------------------------------------------------------------------------------------------

# Queue Method

def levelOrder(root):
    if root is None:
        return
 
    queue = []
 
    queue.append(root)
 
    while(len(queue) > 0):
 
        print(queue[0].data,end=" ")
        node = queue.pop(0)
 
        if node.left is not None:
            queue.append(node.left)
 
        if node.right is not None:
            queue.append(node.right)


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

# LevelOrder(tree)        # recursive method call    and its return method is in file "Recur_Levelorder_return.py"
levelOrder(tree)
