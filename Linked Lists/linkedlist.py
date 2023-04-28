class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    #  Method to print linkedlist
    def show(self):
        first = self.head
        while first is not None:
            print(first.data, end=" ")
            first = first.next

lis = LinkedList()
lis.head = Node(2)
lis.head.next = Node(3)
lis.head.next.next = Node(4)
lis.head.next.next.next = Node(6)
lis.head.next.next.next.next = Node(5)

lis.show()

# print(lis.head.data, lis.head.next.data, lis.head.next.next.data)    # Print element without using show