class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
    
        n = len(A)
        result = 0
    
        # computing sum of subarray
        # using formula
        for i in range(0, n):
            result += (A[i] * (i+1) * (n-i))
    
        # return all subarray sum
        return result