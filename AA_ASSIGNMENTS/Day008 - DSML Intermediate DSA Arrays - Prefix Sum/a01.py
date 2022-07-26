class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)

        arr = [0]*n
        # print(arr)
        arr[0] = A[0]

        for i in range(1,n) :##build prefixing
            arr[i] = arr[i-1] +A[i]
        
        
        if arr[-1]-arr[0]== 0:#edge case all  00000000000000000000000000
                return 0

        for i in range(1,n):
            if arr[i-1] ==arr[-1]-arr[i] :# i bcz lower limit of i+1
                return i

        return -1