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


    #  Iterative method to reverse LL
    def rev(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    
    # Recursive Method to reverse LL
    def reverse(self,current):
        
        if current is None or current.next is None:
            return current
  
        rest = self.reverse(current.next)
  
        current.next.next = current        # Put first element at the end
        current.next = None
  
        return rest             # Fix the head



    def revers(self,head_ref):                # Iterative using two pointers
        current = head_ref
        next= None
        while (current.next != None) :
            next = current.next
            current.next = next.next
            next.next = (head_ref)
            head_ref = next
        
        return head_ref



llist = LinkedList()
llist.appen(0)
llist.appen(4)
llist.appen(9)
llist.appen(3)
llist.appen(6)
llist.appen(8)
llist.appen(1)
llist.appen(2)
llist.show()
print("")


# llist.rev()
# llist.show()

# llist.head = llist.reverse(llist.head)    # Storing new head of linked list
# llist.show()

llist.head = llist.revers(llist.head)    # Storing new head of linked list
llist.show()
