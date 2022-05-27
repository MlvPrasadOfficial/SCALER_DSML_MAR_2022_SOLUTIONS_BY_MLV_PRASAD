
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):

        tree_vals = []

        def inorder(tree):

            if tree:

                inorder(tree.left)
                tree_vals.append(tree.val)
                inorder(tree.right)

        inorder(A)
        return tree_vals
