class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):     
		count = 0
		for i in range(len(A)) :
			res=0
			for j in range(i,len(A)):
				res+=A[j]				
				if ((j-i) % 2 ==1) and res < B :
				    count += 1
				elif ((j-i) % 2 ==0) and res > B :
				    count+= 1
				    
				
		return (count)
		
