class Solution:
    def solve(self, A, B):
        L  = len(A)
        if B == 0 :
            a = []
            for i in range(L) :
                a.append(i)
            return a
        newb = ((2*B)+1)        
        res = 0
        aa = []
        for i in range(newb,L+1):
            pp = A[i-newb:i]         
            count = 0
            for j in range(len(pp)-1):                
                if pp[j]+ pp[j+1]== 1:                    
                    count+=1
            if count == len(pp)-1 :
                aa.append(i-newb +B)
        return aa
            
         
