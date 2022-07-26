class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B = A[-3:]
        B=int(B)
        if B % 8 == 0 :
            return 1
        else :
            return 0
