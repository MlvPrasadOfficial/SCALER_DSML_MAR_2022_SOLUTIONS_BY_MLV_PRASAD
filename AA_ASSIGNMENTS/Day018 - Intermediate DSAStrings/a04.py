class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        A= list(A)
        for i in range(len(A)) :
            if ord(A[i]) >= 97 and ord(A[i]) <= 122 :
                A[i] = chr(ord(A[i])-32)
            
        
        return "".join(A)