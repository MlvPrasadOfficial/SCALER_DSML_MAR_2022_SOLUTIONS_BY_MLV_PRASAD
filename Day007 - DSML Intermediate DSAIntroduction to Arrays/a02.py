class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0 
        for i in range(len(A)) :
            for j in range(len(A)):
                if (i<j)and (A[i]+ A[j]== B):
                    return 1
        return 0
       