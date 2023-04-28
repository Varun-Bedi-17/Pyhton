class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def check_bst(root):
    def chcking(root, left = None, right = None):
        if root is None:
            return True
        

        if left is not None and root.data <=left.data:
            return False

        if right is not None and root.data >=right.data:
            return False

        # print(root.data, left, right)
        return chcking(root.left, left, root) and chcking(root.right, root, right)

    return chcking(root,None, None)

root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(8)
    #root.right.left.left = newNode(40)
if (check_bst(root)):
    print("Is BST")
else:
    print("Not a BST")



tree = Node(5)
tree.left = Node(2)
tree.right = Node(4)
tree.left.left = Node(7)
tree.right.left = Node(8)
tree.right.left.left = Node(9)
tree.right.left.right = Node(6)
tree.right.left.right.right = Node(1)

if (check_bst(tree)):
    print("Is BST")
else:
    print("Not a BST")


#               5
#             /   \
#           2       4
#          / \     /  \
#        7    None 8   None
#                 / \
#                9   6
#                     \
#                      1