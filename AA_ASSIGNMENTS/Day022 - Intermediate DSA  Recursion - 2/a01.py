class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        result = 1
        base = A % C
        while B > 0:
            if B % 2 == 1:
                result = (result*base) % C
            B = B >> 1
            base = (base*base)%C
        return result%C