# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @return an integer
    def solve(self, A, B, C):


        root = A 
        low = B 
        high = C


        if root == None:
            return 0
            

        if root.val == high and root.val == low:
            return 1
    
    
      
        if root.val <= high and root.val >= low:
            return (1 + self.solve(root.left, low, high) +
                        self.solve(root.right, low, high))
    
        elif root.val < low:
            return self.solve(root.right, low, high)
    
        else:
            return self.solve(root.left, low, high)