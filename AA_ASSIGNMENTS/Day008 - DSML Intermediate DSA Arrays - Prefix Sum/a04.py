class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        N = len(A)
        Z = [0]*N
        Z[0]=A[0]
        sol =[]
        for i in range(1,N):## prefix sum
            Z[i] =Z[i-1]+A[i]
        Z.insert(0,0)
        for p,q in B:            
            summ = Z[q]-Z[p-1]            
            sol.append(summ)
        return sol

        