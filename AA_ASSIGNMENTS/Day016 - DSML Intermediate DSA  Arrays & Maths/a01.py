class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        curr_majority = A[0]
        cnt = 1
        for x in A[1:]:

            if x != curr_majority:
                cnt -= 1
            else:
                cnt += 1

            if cnt == 0:
                curr_majority = x
                cnt = 1
                
        return curr_majority
