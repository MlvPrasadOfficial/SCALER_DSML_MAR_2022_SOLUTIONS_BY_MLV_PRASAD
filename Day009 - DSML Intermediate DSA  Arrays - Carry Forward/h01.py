class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        size = len(A)
        count = 0
        for index in range(size):
            if A[index].isalpha() and A[index].lower() in ["a", "e", "i", "o", "u"]:
                count += (size-index)
        return count%10003