class Solution:
    def diagonal(self, A):  
    
        n = len(A)
        N = n + ( n - 1)
    
        result = []        
        for i in range(N) :  # 2n - 1 rows
            result.append([])

        for i in range(n) :
            for j in range(n) :
                result[i + j].append(A[i][j])
                
        for p in range(len(result)):
            while len(result[p]) <n :
                result[p].append(0)
        return result
    
    


