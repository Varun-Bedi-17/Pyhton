
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def appen(self,val):
        if self.head is None:
            self.head = Node(val)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(val)

    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

# Itertion Method
def merge(head1, head2):
    dummy = Node(-1)
    ptr = dummy

    while True:
        if head1 is None:
            ptr.next = head2
            break

        if head2 is None:
            ptr.next = head1
            break
    
        if head1.data < head2.data:
            ptr.next = head1
            head1 = head1.next
        
        else:
            ptr.next = head2
            head2 = head2.next
        
        ptr = ptr.next
    return dummy.next

# Recursive Method
def mergeLists(head1, head2):
    temp = None
  
    if head1 is None:
        return head2

    if head2 is None:
        return head1
  
    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeLists(head1.next, head2)
          
    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)

    return temp
    

s2 = LinkedList()
s2.appen(2)
s2.appen(6)
s2.appen(8)

s3 = LinkedList()
s3.appen(1)
s3.appen(2)
s3.appen(3)
s3.appen(4)
s3.appen(5)

s2.show()
print("")
s3.show()
print("")

s2.head = mergeLists(s2.head,s3.head)
s2.show()