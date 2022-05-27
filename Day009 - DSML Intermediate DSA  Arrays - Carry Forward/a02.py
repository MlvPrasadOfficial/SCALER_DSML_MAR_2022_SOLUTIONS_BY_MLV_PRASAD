class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        inf = 100000000000
        min_ele=min(A)
        max_ele=max(A)
        last_min=-inf
        last_max=-inf/2
        result=inf
        c=0
        for i in A:
            if(i == min_ele):
                last_min=c
            if(i == max_ele):
                last_max=c
            p=abs(last_min - last_max) + 1
            if(result > p):
                result=p
            c=c+1
            ###result = min(result, abs(last_min - last_max) + 1)
        return result