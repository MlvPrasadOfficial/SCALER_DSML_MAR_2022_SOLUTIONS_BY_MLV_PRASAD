class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        st = []
        for i in range(A):
            if C[i] == 0:
                st.pop()
            else:
                st.append(C[i])
        if len(st) != 0:
            return st[-1]
        else:
            return B