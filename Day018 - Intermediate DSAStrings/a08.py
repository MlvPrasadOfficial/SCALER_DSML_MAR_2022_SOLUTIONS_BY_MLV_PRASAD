class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A= list(A)
        for i in range(len(A)) :
            if ord(A[i]) >= 97 and ord(A[i]) <= 122 :
                A[i] = chr(ord(A[i])-32)
            else :
                A[i] = chr(ord(A[i])+32)
        
        return "".join(A)
            