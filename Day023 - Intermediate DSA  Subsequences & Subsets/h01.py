class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        N = len(A)
        if N==1:
            return 1
        count = 1
        temp = 1-(A[0]%2)
        for i in range(1,len(A)):
            if A[i]%2==temp:
                count += 1
                temp = 1-(A[i]%2)
                
        return count