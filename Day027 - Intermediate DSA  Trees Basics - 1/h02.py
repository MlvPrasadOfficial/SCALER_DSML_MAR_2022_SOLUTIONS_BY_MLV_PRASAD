# Definition for a  binary tree node
# class TreeNode:
#    def _init_(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
# global node_count
class Solution:
    # @param A : root node of tree
    # @return an integer
    global node_count
    def ancestor_check(self,A,max_ancestor):
        if A == None:
            return 
        elif A.val > max_ancestor:
            max_ancestor = A.val
            global node_count 
            node_count += 1
        self.ancestor_check(A.left,max_ancestor)
        self.ancestor_check(A.right,max_ancestor)

    def solve(self, A):
        global node_count
        node_count = 0
        self.ancestor_check(A,0)
        return node_count