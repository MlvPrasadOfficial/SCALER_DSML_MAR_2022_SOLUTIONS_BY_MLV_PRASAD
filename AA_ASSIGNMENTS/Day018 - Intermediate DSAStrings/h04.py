class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A+A      

        A= list(A)
        
        A=[item for item in A if not ( item.isupper())]
        
        for j in range(len(A)) :
            # if ( A[j] == "a" ) or (A[j] == "e") or (A[j] == "i") or (A[j] == "o") or (A[j] == "u") :
            if (A[j] in "aeiou") :
                A[j]  = "#"           
            
        
        return "".join(A)