class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def findMod(self, A, B):
        ans = 0
        mod = B
        n = len(A)
        curr = 1
        for i in range(n - 1, -1, -1):
            dig = ord(A[i]) - 48
            term = (dig * curr) % mod
            ans = (ans + term) % mod
            curr = (curr * 10) % mod
        return ans
