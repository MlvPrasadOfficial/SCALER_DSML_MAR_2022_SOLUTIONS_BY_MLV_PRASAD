class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort(reverse = True)
        res = []        
        for i in range(len(A)):
            x =  [A[i]]
            n = [x + y for y in res]
            if len(res) != 0:
                res += n
            res += [x]
            # print(A[i], res)            
        res.append([])
        res.reverse()
        return res
