class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        mm=[]
        index = 0
        result = 0
        res = 0

        for i in range(n):
            curr_count = 0            
            zz = i

            while( i <n and A[i]>= 0):
                curr_count += 1
                i += 1
            
            if curr_count > res :
                index = zz
            res = max(res, curr_count)
            
        start = index
        end = index + res
        return (A[start : end])
