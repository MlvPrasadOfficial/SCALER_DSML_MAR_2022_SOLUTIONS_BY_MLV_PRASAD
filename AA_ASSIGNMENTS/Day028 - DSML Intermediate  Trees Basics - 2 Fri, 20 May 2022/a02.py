class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if not A:
            return
        if A.left and A.right:
            A.left,A.right = A.right,A.left
        
        self.invertTree(A.left)
        self.invertTree(A.right)
        
        return A