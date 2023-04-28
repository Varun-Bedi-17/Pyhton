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

    def alternate(self, head, value):
        if head is None:
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
        if current:
            head.next = current
        while current and k < (2*value)-1:
            current = current.next
            k += 1
        if current is not None:
            current.next = self.alternate(current.next,value)
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
llist.appen(10)
llist.appen(12)
llist.appen(13)


llist.show()
print("")

llist.head = llist.alternate(llist.head,3)
llist.show()