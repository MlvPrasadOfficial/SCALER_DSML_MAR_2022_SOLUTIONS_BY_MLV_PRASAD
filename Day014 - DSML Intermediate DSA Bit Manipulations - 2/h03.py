class Solution:
    # @param A : list of integers
    # @return an integer
    def compressBits(self, A):
        xor = A[0]
        for i in range(1,len(A)):
            xor = xor ^ A[i]
        return xor
