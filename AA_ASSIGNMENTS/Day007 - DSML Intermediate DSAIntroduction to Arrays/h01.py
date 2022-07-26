class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A = sorted(A)
        # print(A)
        if B not in  A :
            return -1
        count = 0
        for i in range(len(A)) :
            if B < A[i] :
                count += 1
        return count
        # return count
        #    s