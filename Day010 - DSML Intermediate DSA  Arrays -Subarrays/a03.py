class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):    
        n = len(A) # 7       
        if (n < B):
             return 0
        res_index = 0
        
        curr_sum = 0
        for i in range(B):
            curr_sum += A[i]   # 100

        min_sum = curr_sum   # 100
        for i in range(B, n):  # 3, 7
            curr_sum += A[i] - A[i-B]
            if (curr_sum < min_sum):
            
                min_sum = curr_sum
                res_index = (i - B + 1)
        return res_index
            
    