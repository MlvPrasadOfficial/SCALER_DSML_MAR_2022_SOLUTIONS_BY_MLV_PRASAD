class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    # global count 
    # count = 0
    def solve(self, A, B):
        if A  == None and B == None:
            return 0
        if A == None or B == None or A.val != B.val:
            return -1
        ans = -1
        s1 = self.solve(A.left,B.left)
        s2 = self.solve(A.right,B.right)
        s = -1
        if s1 != -1 and s2 != -1:
            ans= s1+s2
        
        s1 = self.solve(A.left,B.right)
        s2 = self.solve(A.right,B.left)
        # p = -1
        if s1 != -1 and s2 != -1:
            p= s1+s2+1
            if ans == -1 or ans > p:
                ans = p
        
        # if s != -1:
        #     ans = s
        # if ans == -1 or p < ans:
        #     ans = p 
        return ans