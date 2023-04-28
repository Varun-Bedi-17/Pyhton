#  Breadth-First Traversal -- Level Order Traversal
#  Depth-First Traversal -- Inorder, Preorder, Postorder

class Node():
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return []
    return ([root.data] + preorder(root.left) + preorder(root.right))

def inorder(root):
    if root is None:
        return []
    return (inorder(root.left) + [root.data] + inorder(root.right))

def postorder(root):
    if root is None:
        return []
    return (postorder(root.left) + postorder(root.right) + [root.data])





tree = Node(5)
tree.left = Node(2)
tree.right = Node(4)
tree.left.left = Node(7)
tree.right.left = Node(8)

#               5
#             /   \
#           2       4
#          / \     /  \
#        7    None 8   None

print(preorder(tree))
print(inorder(tree))
print(postorder(tree))




tree2 = Node(1)
tree2.left = Node(2)
tree2.right = Node(3)
tree2.left.left = Node(4)
tree2.left.right = Node(5)
tree2.right.left = Node(8)

#               1
#             /   \
#           2       3
#          / \     /  
#        4    5  8   

print(preorder(tree2))
print(inorder(tree2))
print(postorder(tree2))