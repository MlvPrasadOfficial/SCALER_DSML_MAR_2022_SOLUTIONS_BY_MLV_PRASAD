class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):


        from math import ceil, log2
    

        n =  A
        x = '1'
        y = '2'
    
        # Calculate the length from above 
        # formula as discussed above 
        length = ceil(log2(n + 2)) - 1; 
    
        # Calculate rank for length L 
        rank = n - (1 << length) + 1; 
    
        left = ""; right = ""; 
    
        for i in range(length - 1 , -1, -1):
    
            # Mask to check if i't bit 
            # is set or not 
            mask = (1 << i); 
    
            # If bit is set append '5' 
            # else append '4' 
            bit = (mask & rank); 
    
            if (bit) :
                left += y; 
                right += y; 
                
            else :
                left += x; 
                right += x; 
    
        right = right[::-1];
        
        res = left + right;
        return res;