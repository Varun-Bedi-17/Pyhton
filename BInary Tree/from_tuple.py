class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def fromTuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        root = Node(data[1])
        root.left = fromTuple(data[0])
        root.right = fromTuple(data[2])
    
    elif data is None:      # so that no new variable of None node is created
        root = None

    else:
        root = Node(data)
    
    return root

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.data))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.data))
    display_keys(node.left,space, level+1)   


tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7,8)))
tree = fromTuple(tree_tuple)
display_keys(tree)