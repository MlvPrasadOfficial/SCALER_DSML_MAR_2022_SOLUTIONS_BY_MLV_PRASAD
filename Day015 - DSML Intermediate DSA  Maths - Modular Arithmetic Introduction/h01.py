class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        m= [A,B,C]
        m = sorted(m)
        # return m
        a = ""
        for i in range(3):
            a = a + (str((m[i])))
        return a

