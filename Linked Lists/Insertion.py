class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    
    # Insert at first position
    def insert1(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    
    # Insert a node after given node
    def insert(self, pos, val):
        if pos is None:
            print("Node is not present")
            return
        new_node = Node(val)
        new_node.next = pos.next
        pos.next = new_node
        
        




    # Insert element at last position
    def appen(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(val)

    
    #  Method to print linkedlist
    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next




s2 = LinkedList()
s2.appen(2)
s2.appen(8)
s2.appen(6)
# s2.show()


s2.insert1(5)
s2.insert1(3)
# s2.show()

s2.insert(s2.head.next.next, 3)
s2.show()

        