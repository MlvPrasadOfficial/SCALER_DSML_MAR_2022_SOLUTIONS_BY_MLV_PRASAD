class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        N = len(A)       	
	    max_so_far =A[0]
        curr_max = A[0]
        
        for i in range(1,N):
            curr_max = max(A[i], curr_max + A[i])  ##1
            max_so_far = max(max_so_far,curr_max)  ##2
            
        return max_so_far 
        #
