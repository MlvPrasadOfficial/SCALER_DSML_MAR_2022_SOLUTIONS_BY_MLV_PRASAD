
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def cnt(n):
            return (n * (n + 1)) // 2
        MOD = int(1e9 + 7)
        ans = 0
        n = len(A)
        for b in range(27):
            c = 0
            C = cnt(n)
            for i in range(n):
                if A[i] & 1:
                    C -= cnt(c)
                    c = 0
                else:
                    c += 1
                A[i] >>= 1
            C -= cnt(c)
            ans = (ans + (1 << b) * C) % MOD
        return ans