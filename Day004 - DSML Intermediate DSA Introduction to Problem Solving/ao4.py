class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        for i in range(1,10001):
            if i*i == A:
                return i
        return -1