class Solution:
    def sortColors(self, A):      
        
        num0 = 0
        num1 = 0
        num2 = 0
        for i in range(len(A)):
            if A[i]==0:
                num0 += 1
            if A[i]==1:
                num1 += 1
            if A[i]==2:
                num2 += 1
                
        for i in range(num0):
            A[i]=0
        for i in range(num0,num0+num1):
            A[i]=1
        for i in range(num0+num1,num0+num1+num2):
            A[i]=2
            
        return A
