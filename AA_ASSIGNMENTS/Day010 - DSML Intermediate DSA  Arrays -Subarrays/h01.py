class Solution:
    def solve(self, A, B):
        n = len(A)
        dp = [0] * (n+1)
        for i in range(n):### PREFIC SUM OF ARRAY
            dp[i+1]=dp[i]+A[i]
        ans = 0


        for i in range(n):
            for j in range(i,n):
                val = dp[j+1]-dp[i]
                if val<B:
                     ans+=1
        return ans