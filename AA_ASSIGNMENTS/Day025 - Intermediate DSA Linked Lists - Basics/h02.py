# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        head = A
        depth = 1
        nodes = {}
        while head : 
            nodes[depth] = head.val
            head = head.next
            depth += 1

        return nodes[(depth//2) + 1] if depth%2 else nodes[(depth//2)]