class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B = "bob"
        count = 0
        for i in range(len(A)-2) :
            if A[i:i+3] == B :
                count += 1
        return count
