class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
    
        result = 0;
        for B in range(len(A)):
            result *= 26
            result += ord(A[B]) - ord('A') + 1
    
        return result