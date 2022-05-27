# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
        head = A
        if not head:
            return head
        dummy = op = ListNode(0)
        while head.next:
            if head.val != head.next.val:
                op.next = head
                op = op.next
            head = head.next
        op.next = head
        return dummy.next