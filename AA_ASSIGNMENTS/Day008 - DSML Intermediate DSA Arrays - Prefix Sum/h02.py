class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        pro = 1
        for i in range(len(A)):
            # B[i] =B[i-1]*A[i]
            pro = pro *A[i]
        # print(pro)
        B=[0]*len(A)
        for j in range(len(A)):
            B[j]=int(pro/A[j])
        return B