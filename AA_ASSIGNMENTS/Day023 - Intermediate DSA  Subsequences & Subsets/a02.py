class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        start = -1
        for char in A:
            temp = B.find(char, start+1)
           
            if temp == -1:
                return "NO"
            else:
                start = temp
       
        return 'YES'
