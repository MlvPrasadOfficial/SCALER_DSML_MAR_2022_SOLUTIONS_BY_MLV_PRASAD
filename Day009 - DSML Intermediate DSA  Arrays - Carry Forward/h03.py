class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        # ans = 1 ####rightost so 1
        maxi = A[-1]
        
        out =[maxi] #last already leader

        for i in range(n-2,-1,-1):
            if A[i] > maxi :
                # ans =+ 1
                maxi = A[i]
                out.append(maxi)
        return out

