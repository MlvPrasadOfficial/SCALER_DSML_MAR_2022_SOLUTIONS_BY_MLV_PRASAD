class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B in A :
            return 1
        if(B == 0):
            return 1
        pow = (int(2**len(A)))
        for i in range(pow) :
            x = 0
            sum = 0
            num = i
            while num > 0 :
                if num & 1 == 1:
                    sum += A[x]
                x +=1
                num = num >> 1
            if(sum == B):
                return 1
        return 0

