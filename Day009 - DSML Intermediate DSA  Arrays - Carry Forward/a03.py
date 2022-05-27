class Solution:
	def bulbs(self, A):
        count = 0
        
        n = len(A)
        for i in range(n):
            if (A[i] == 1 and count % 2 == 0):
                continue     
            elif(A[i] == 0 and count % 2 != 0):
                continue
    
            
            elif (A[i] == 1 and count % 2 != 0):    ###if 1 then count odd            
                count += 1  
            elif (A[i] == 0 and count % 2 == 0):    #### of 0 then count even
                count += 1
            else :
                pass
        return count
 