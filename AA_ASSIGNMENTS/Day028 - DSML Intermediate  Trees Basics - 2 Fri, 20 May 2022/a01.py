class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
    # def isSymmetric(self, root: TreeNode) -> bool:
        root = A
        return self.isMirror(root, root)
    
    
    def isMirror(self, t1, t2):
        if not t1 and not t2:
             return 1
        if not t1 or not t2: 
            return 0
        if t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right) :
            return 1
        else :
            return 0