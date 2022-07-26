class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        r = A[1]-A[0] # diff
        for i in range(1,len(A)):
            if A[i]== (A[0]+(r*i)) :## check every step
                pass
            else :
                return 0
        return 1
            
