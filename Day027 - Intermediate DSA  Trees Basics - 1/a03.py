class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):

        
        traversal, stack = [], [A]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]