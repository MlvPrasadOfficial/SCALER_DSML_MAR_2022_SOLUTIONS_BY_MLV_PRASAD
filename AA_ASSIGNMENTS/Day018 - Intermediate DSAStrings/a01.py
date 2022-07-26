class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = list(A.split())
        A = A[::-1]
        return " ".join(A)
