class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    
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

    
    # Reverse k nodes in LL
    def revers(self, head, value):

        if head == None:
            return 
        k = 0
        current = head
        prev = None
        
        while current and k < value:
            next = current.next
            current.next = prev
            prev = current
            current = next
            k += 1
        
        if next is not None:
            head.next = self.revers(next, value)

        return prev

llist = LinkedList()
llist.appen(4)
llist.appen(9)
llist.appen(0)
llist.appen(2)
llist.appen(6)
llist.appen(1)
llist.appen(8)
llist.appen(3)

llist.show()
print("")

llist.head = llist.revers(llist.head, 3)
llist.show()