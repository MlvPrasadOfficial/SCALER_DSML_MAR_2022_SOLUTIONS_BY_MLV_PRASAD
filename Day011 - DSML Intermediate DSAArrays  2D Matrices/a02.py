class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        m = len(A)
        n = len(A[0])
        coulmn=[]

        for col in range(n):
            summ = 0
            for row in range(m) :
                summ += A[row][col]

            coulmn.append(summ)

        return coulmn

