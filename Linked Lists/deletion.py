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


    # Deletion of node
    def delete(self, value):
        current = self.head
        if current is not None:
            if current.data == value:
                self.head = current.next
                current = None
                return
        
        while current:
            if current.data == value:
                break
            prev = current
            current = current.next
        
        if current == None:
            return

        prev.next = current.next
        current = None


    # Method to find length of LL
    def length(self):
        current = self.head
        result = 0
        while current:
            result += 1
            current = current.next
        return result


    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


    #  Detection of loop in LL
    def detect_loop(self):
        l = []
        current = self.head
        while current:
            if current in l:
                return "Loop Found"
            l.append(current)
            current = current.next
        return "Loop not Found"


    #  Detection of loop and find length in LL
    def detect_len_loop(self):
        l = []
        current = self.head
        while current:
            if current in l:
                ind = l.index(current)
                length = l[ind:]
                return f"Loop Found and the length of loop is {len(length)}"
            l.append(current)
            current = current.next
        return "Loop not Found"

    
    
# Removal of cycle in LL    
    def remove_loop(self):
        l = []
        current = self.head
        while current:
            if current in l:
                prev.next = None
                return "Loop Found"
            l.append(current)
            prev = current
            current = current.next
        return "Loop not Found"


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

# llist.delete(5)
# llist.show()

# print(llist.length())

# print(llist.get_element(3))

# print(llist.detect_loop())

# llist.head.next.next.next.next.next.next.next.next = llist.head.next
# print(llist.detect_loop())

# llist.head.next.next.next.next.next.next.next.next = llist.head.next
# print(llist.detect_len_loop())

# llist.head.next.next.next.next.next.next.next.next = llist.head.next
# print(llist.remove_loop())
# llist.show()

