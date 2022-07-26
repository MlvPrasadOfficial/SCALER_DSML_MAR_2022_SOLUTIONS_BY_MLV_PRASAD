class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A= sorted(A)
        # print(A)
        count = 0
        for i in A:
            zz = (A[-1]-i)
            count += zz
        
        return count
