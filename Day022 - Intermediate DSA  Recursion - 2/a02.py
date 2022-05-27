def sum_of_digit( n ): 
    if n == 0: 
        return 0
    return (n % 10 + sum_of_digit(int(n / 10))) 
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return sum_of_digit(A)