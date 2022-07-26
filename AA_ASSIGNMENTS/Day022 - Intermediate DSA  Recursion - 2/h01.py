class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = A
        k = B
        if n==0 and k==1:
            return 0
        mid = pow(2, n-1)
        if k<=mid:
            return self.solve(n-1, k)
        else:
            return int(not self.solve(n-1, k-mid))