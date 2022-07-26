class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == B :
            return A 
        if A > B :
            n = A-B
            return n
        else :
            n = B- A 
            return n