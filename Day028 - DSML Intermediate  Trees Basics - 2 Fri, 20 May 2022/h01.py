class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        res = []
        def xoxo(A,lis,B):
            if not A:
                return False
            if A.val == B:
                lis.append(A.val)
                for i in lis:
                    res.append(i)
            A.left = xoxo(A.left,lis+[A.val],B)
            A.right = xoxo(A.right,lis+[A.val],B)
        xoxo(A,[],B)
        return res 