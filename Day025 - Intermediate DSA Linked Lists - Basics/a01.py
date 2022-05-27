class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

llist = LinkedList()

def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    if position == 1:
        node = Node(value)
        node.next = llist.head
        llist.head = node
    else:
        current = llist.head
        temp = Node(value)
        i = 1
        while current.next != None and i < position-1:
            current = current.next
            i += 1
        # if current.next == None:
        #     current.next = temp
        temp.next = current.next
        current.next = temp
        
def delete_node(position):
    # @param position, integer
    # @return an integer
    if position == 1:
        llist.head = llist.head.next
    else:
        current = llist.head
        i = 1
        while current.next != None and i < position-1:
            current = current.next
            i += 1
        if current.next == None:
            return  
        else:
            current.next = current.next.next
        


def print_ll():
    # Output each element followed by a space
    if llist.head == None:
        return None
    else:
        current = llist.head
        while current:
            if current.next==None:
                print(current.value)
            else:
                print(current.value, end =' ')
            current=current.next