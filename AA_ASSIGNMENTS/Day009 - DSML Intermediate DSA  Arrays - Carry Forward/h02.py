class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):

        if (len(A) % 2 != 0) or (A[0] % 2!=0 ) or ( A[-1]%2!=0) :
            ## odd length,or first or last elemet should be odd
            return "NO" 
                   
        else :
            return "YES"
        