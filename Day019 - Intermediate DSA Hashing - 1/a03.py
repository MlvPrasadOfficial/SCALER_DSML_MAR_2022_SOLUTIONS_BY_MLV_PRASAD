class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d = {}
        curr_sum = 0
        for x in A:
            curr_sum += x
            if curr_sum == 0 or x == 0 or curr_sum in d:
                return 1
            else:
                d[curr_sum] = 1
        return 0