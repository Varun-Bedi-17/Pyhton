class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def chck_Complete(root):
 
    if root is None:
        return True
 
    # create an empty queue and enqueue the root node
    queue = []
    queue.append(root)
 
    # flag to mark the end of full nodes
    flag = False
 
    # loop till queue is empty
    while queue:
 
        # dequeue front node
        node = queue.pop(0)
 
        # if we have encountered a non-full node before and the current node
        # is not a leaf, a tree cannot be complete
        if flag and (node.left or node.right):
            return False
 
        # if the left child is empty and the right child exists,
        # a tree cannot be complete
        if node.left is None and node.right:
            return False
 
        # if the left child exists, enqueue it
        if node.left:
            queue.append(node.left)
 
        # if the current node is a non-full node, set the flag to true
        else:
            flag = True
 
        # if the right child exists, enqueue it
        if node.right:
            queue.append(node.right)
 
        # if the current node is a non-full node, set the flag to true
        else:
            flag = True
 
    return True


# ---------------------------------------------------------------------------------------
# Recursive method

def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

def isComplete(root, i, n):
 
    # return if the tree is empty
    if root is None:
        return True
 
    if (root.left and 2*i + 1 >= n) or not isComplete(root.left, 2*i + 1, n):
        return False
 
    if (root.right and 2*i + 2 >= n) or not isComplete(root.right, 2*i + 2, n):
        return False
 
    return True



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
print(isComplete(tree,0,size(tree)))


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

print(isComplete(root,0,size(root)))