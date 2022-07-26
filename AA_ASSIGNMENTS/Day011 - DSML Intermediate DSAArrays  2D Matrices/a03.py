class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        p = len(A) # A R
        q = len(B[0]) # B C

        result = [[0]*q for _ in range(p)]
        for i in range(len(A)):            
            for j in range(len(B[0])):                
                for k in range(len(B)):# OR LEN(A[0])
                    result[i][j] += A[i][k] * B[k][j]

        
        return result