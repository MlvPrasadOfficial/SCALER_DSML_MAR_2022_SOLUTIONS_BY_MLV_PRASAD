class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        m =len(A)

        summ = 0
        for i in range(m):
            j = i
            summ += A[i][j]

        return summ

