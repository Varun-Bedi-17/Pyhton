class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def chck_full(root):     
    if (root.right is None and root.left is not None) or (root.left is None and root.right is not None):
        return False
    if root.left is None and root.right is None:
        return True
    # chck_l = chck_full(root.left)
    # chck_r = chck_full(root.right)
    # return chck_l and chck_r
    return chck_full(root.left) and chck_full(root.right)


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
print(chck_full(tree))


root = Node(10)
root.left = Node(20)
root.right = Node(30)
 
root.left.right = Node(40)
root.left.left = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
 
root.left.left.left = Node(80)
root.left.left.right = Node(90)
root.left.right.left = Node(80)
root.left.right.right = Node(90)
root.right.left.left = Node(80)
root.right.left.right = Node(90)
root.right.right.left = Node(80)
root.right.right.right = Node(90)

print(chck_full(root))