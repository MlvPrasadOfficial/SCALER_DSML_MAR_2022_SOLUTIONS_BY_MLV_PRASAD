class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        xor = A[0]
        for i in range(1,len(A)):
            xor = xor ^ A[i]

        return xor
