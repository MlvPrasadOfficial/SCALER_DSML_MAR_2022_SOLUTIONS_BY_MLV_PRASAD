class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        arr = []
        while A > 0 : # decimal to binary
            r = A %2
            arr.append(r)
            A //= 2
        
        return sum(arr)
