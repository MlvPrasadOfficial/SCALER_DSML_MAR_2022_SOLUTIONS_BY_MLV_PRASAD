class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):


        if A is None:
            return []
        
        stack, output = [A, ], []
        
        while stack:
            A = stack.pop()
            if A is not None:
                output.append(A.val)
                if A.right is not None:
                    stack.append(A.right)
                if A.left is not None:
                    stack.append(A.left)
        
        return output