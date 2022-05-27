class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
        N = A
        row = 0
        col = 0
        B = [[ 0 for i in range(N)] for j in range(N)]
        x = 1
        
        
        while N > 1:
            # l to R:
            for i in range(col, col + N - 1):
                B[row][i] = x
                x+=1
            # top to  bottom
            for i in range(row,row+N-1):
                B[i][col +N -1] =x
                x+=1
            # right to left
            for i  in range(col +N-1,col,-1):
                B[row+N-1][i]=x
                x+=1
            #from bottom to top
            for i in range(row +N -1,row,-1):
                B[i][col]= x
                x+=1
                
            
            N = N -2
            row += 1
            col += 1
            
        if A %2 == 1:
            B[A//2][A//2]=A*A
            
        
        
        
        
        return B 