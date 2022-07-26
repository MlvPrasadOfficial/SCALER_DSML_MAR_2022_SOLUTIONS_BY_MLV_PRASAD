class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        m = len(A)
        n = len(A[0])
        res = [[0]*n for _ in range(m)]# empty identical matrix

        for i  in range(m):
            for j in range(n):
                res[i][j] = A[i][j] - B[i][j]
        

        return res
