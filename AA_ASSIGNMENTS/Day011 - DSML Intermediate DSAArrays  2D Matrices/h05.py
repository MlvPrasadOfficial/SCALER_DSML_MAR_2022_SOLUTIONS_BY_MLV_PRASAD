class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
    
        sum = 0
        
        for i in range( N):
            sum += A[i][N - 1 - i] #j,, i +1 + j + 1 = N + 1

    
        return sum