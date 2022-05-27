class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        mA =len(A)
        nA = len(A[0])

        # mB = len(B)
        # nB = len(B[0])
        # if mA != mB or nA != nB :
        #     return 0
        # else :
    

        for i in range(mA):
            for j in range(nA):
                if (A[i][j] != B[i][j]):
                    return 0
        return 1
