class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        m = len(A)
        n = len(A[0])
        res = [[0]*m for _ in range(n)] #empty matrix transpose so C * R

        for i  in range(m):
            for j in range(n):
                res[j][i] = A[i][j]
        

        return res
