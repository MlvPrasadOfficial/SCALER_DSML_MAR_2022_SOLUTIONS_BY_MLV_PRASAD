class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        minchar = 'z'
        idx = 1000000000
        for i in range(len(A) - 1):
            if A[i] < minchar:
                minchar = A[i]
                idx = i
        
        minchar2 = 'z'
        for i in range(idx + 1, len(A)):
            if(A[i] < minchar2):
                minchar2 = A[i]
        
        ans = minchar + minchar2
        return ans