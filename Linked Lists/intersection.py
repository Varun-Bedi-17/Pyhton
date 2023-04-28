class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

# Two loop method
def intersect(head1, head2):
    if head1 == None or head2 == None:
        return None
    
    while head1:
        temp = head2
        while temp:
            if temp == head1:
                return temp.data
            temp = temp.next
        head1 = head1.next
    return None


# Difference method

def length(head):
    curr = head
    count = 0
    while curr:
        curr = curr.next
        count += 1
    return count

def intersectio(head1,head2):
    l1 = length(head1)
    l2 = length(head2)

    if l1 > l2:
        d = l1-l2
        return intersec(d,head1,head2)
    else:
        d = l2 - l1
        return intersec(d,head2,head1)

def intersec(d,head1,head2):
    for i in range(d):
        if head1 is None:
            return -1
        head1 = head1.next
        
    while head1 is not None or head2 is not None:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next
    return -1


newNode = Node(10)
head1 = newNode
newNode = Node(3)
head2 = newNode
newNode = Node(6)
head2.next = newNode
newNode = Node(9)
head2.next.next = newNode
newNode = Node(15)
head1.next = newNode
head2.next.next.next = newNode
newNode = Node(30)
head1.next.next = newNode

# print(intersect(head1,head2))

print(intersectio(head1,head2))



