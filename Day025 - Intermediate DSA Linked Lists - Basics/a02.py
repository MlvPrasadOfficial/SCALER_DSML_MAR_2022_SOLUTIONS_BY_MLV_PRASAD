# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

# Definition for singly-linked list.
# class ListNode:
#    def _init_(self, x):
#        self.val = x
#        self.next = None
class LinkedList:
    def _init_(self):
        self.head = None

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(self, A):
        llist = LinkedList()
        llist.head = None
        for i in range(len(A)):
            if A[i][0] == 0:
                #insert at head
                new_node = ListNode(A[i][1])
                if llist.head == None:
                    llist.head = new_node
                else:
                    new_node.next = llist.head
                    llist.head = new_node
                temp = llist.head

            elif A[i][0] == 1:
                #insert at end
                new_node = ListNode(A[i][1])
                if llist.head == None:
                    llist.head = new_node
                else:
                    curr = llist.head
                    while curr.next != None:
                        curr = curr.next
                    curr.next = new_node

            elif A[i][0] == 2:
                #append at index A[i][2]
                pos = A[i][2]
                curr_pos = 0
                curr = llist.head
                new_node = ListNode(A[i][1])
                if pos == 0:
                    new_node.next = llist.head
                    llist.head = new_node
                else:
                    while curr:
                        if curr_pos == pos-1:
                            new_node.next = curr.next
                            curr.next = new_node
                            break
                        else:
                            curr_pos += 1
                            curr = curr.next

            elif A[i][0] == 3:
                #delete at index A[i][1]
                prev = None
                if A[i][1] == 0:
                    llist.head = llist.head.next
                else:
                    curr = llist.head
                    pos = A[i][1]
                    curr_pos = 0
                    while curr:
                        if pos == curr_pos:
                            prev.next = curr.next
                            break
                        else:
                            curr_pos += 1
                            prev = curr
                            curr = curr.next
        return llist.head