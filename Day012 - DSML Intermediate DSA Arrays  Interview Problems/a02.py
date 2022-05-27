class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        if n<3 :
            return -1
        cc=[]
        answer=[]
        for i in range(1,n-1):
            middle=A[i]
            cl =[]          
            for j in range(i):
                if A[j]< middle :
                    cl.append(B[j]) 

            cr=[]
            for k in range(i+1,n):
                if A[k]> middle:                    
                    cr.append(B[k])
                    
            if len(cl)== 0 or len(cr)==0:
                pass
            else :
                ans = min(cl)+ min(cr) +B[i]
                answer.append(ans)
            # print(ans)
            
        if len(answer) == 0:
            return -1
        else :
            return min(answer)
        
        
