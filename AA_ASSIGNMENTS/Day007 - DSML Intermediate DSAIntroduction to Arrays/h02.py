class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return -1
        A.sort()
        return A[-2]
