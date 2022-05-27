class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        ctr = 0
        
        for i in range(len(A)):
            
            # Check if element is odd
            if A[i] % 2 == 1:
                ctr += 1
                
        # According to the logic
        # in above approach
        if ctr % 2 == 1:
            return 'No'
        else :
            return 'Yes'