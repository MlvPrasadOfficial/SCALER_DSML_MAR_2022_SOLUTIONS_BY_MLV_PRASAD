# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
#         # N  = len(A)
        # count_g = 0
        # ans = 0
        # numA = [0]*len(A)
        
        # for i in range(N-1,-1,-1):
        #     if A[i] == "G":
        #         count_g +=1
        #     numA[i]=count_g
        
        
        # for j in range(len(A)-1) :
        #     if A[j] == "A":
        #         ans += numA[j]
        # return ans
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        mod = 1000*1000*1000 + 7
        # create an array to store number of G's from i to n
        count_G = [0]*n
        # initialize the array with 0
        for i in range(0, n):
            count_G[i] = 0
        # set the value of count_G[n-1] equal to 1 if last character is G
        count_G[n-1] = (A[n-1] == 'G')
        # traverse the string from backward and count number of G's from i to n
        for i in range(n-2, 0, -1):
            count_G[i] = count_G[i+1] + (A[i] == 'G')
        ans = 0
        # traverse the string again from beginning
        for i in range(0, n-1):
            # if current character is "A" then add number of G's after that 
            if(A[i] == 'A'):
                ans = (ans + count_G[i+1]) % mod
        # return the answer
        return ans



