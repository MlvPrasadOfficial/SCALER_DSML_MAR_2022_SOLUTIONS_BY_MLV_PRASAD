class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A): #dec to bin
        arr = []
        while A > 0 :
            r = A  % 2
            arr.append(r)
            A = A // 2
        return sum(arr)
        
