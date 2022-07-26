class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 1
        def fac(n):
            if n==1:
                return 1
            # break
            return n * fac(n-1)
        return fac(A)