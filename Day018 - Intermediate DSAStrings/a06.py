class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        A= list(A)
        for i in range(len(A)) :
            if ord(A[i]) >= 97 and ord(A[i]) <= 122 :
                # A[i] = chr(ord(A[i])-32)
                pass
            elif  ord(A[i]) >= 65 and ord(A[i]) <= 90:
                pass
            else : 
                return 0
        return 1
