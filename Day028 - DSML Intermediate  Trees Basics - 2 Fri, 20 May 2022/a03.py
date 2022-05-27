class Solution:
	def isValidBST(self, A):
        root = A

        if not root:
            return 1

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return 0
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return 1