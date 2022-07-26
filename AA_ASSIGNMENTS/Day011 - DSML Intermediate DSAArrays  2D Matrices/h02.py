class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        m = len(A)
        n = len(A[0])
        rowsum=[]

        for row in range(m):
            summ = 0
            for col in range(n) :
                summ += A[row][col]

            rowsum.append(summ)

        return rowsum
