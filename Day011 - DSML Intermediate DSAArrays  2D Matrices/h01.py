class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        M = len(A)
        N = len(A[0])
            
        for i in range( M):
            for j in range( N):
                A[i][j] = A[i][j] * B
        return A
