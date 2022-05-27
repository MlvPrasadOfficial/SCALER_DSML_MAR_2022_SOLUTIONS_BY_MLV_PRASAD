class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        suff = [0] * (n + 1)
        suff[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = A[i] + suff[i + 1]
        prefSum = 0
        ans = suff[n - B]
        for i in range(B):
            prefSum = prefSum + A[i]
            suffSum = suff[n - B + i + 1]
            ans = max(ans, prefSum + suffSum)
        return ans

