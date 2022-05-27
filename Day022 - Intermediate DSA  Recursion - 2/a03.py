class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        n = A

        sum = 0;
        
        # Note that the loop
        # continues if n is 0
        # and sum is non-zero.
        # It stops when n becomes
        # 0 and sum becomes single
        # digit.
        while (n > 0 or sum > 9):
            if (n == 0):
                n = sum;
                sum = 0;
            sum = sum + n % 10;
            n = int(n / 10);
            
        # Return true if
        # sum becomes 1.
        return 1 if (sum == 1) else 0