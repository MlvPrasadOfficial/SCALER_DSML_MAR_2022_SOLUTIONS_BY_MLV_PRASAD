class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        A.sort()       
        pow = 1
        mod = 1000000007
        output = 0
        for i in range(len(A)) :     
            output = (output + A[i] * pow - A[len(A)-1-i] * pow) % mod
            pow = pow * 2 % mod      

        return (int((output + mod) % mod))
