class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        maxlist = []
        minlist = []
        for i in range(len(A)) :
            if A[i] %2 ==0:
                maxlist.append(A[i])
            else :
                minlist.append(A[i])
        
        minn = min(minlist)
        maxx = max(maxlist) 
        return maxx - minn
