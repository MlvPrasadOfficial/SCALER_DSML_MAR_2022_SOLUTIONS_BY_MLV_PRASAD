class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        C=A[:B]
        D=A[B:]

        return C[::-1]+D

