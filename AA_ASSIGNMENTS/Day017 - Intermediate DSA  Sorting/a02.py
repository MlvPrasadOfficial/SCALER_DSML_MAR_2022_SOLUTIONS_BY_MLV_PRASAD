class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse = True)## form max to min

        """
        for 6 1 3 4
        6 4 3 1
          4 3 1
            3 1
              1  so max element intlo index
        """
        # print(A)
        ans = 0
        for i in range(len(A)):
            ans += A[i]*(i+1)
        return ans
