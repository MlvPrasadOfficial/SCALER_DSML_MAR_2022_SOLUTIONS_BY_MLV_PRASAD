class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        string  = A
        level = 0
        for c in string:
            if c == "(":
                level += 1
            else:
                level -= 1
            if level < 0:
                return 0
        
        if level != 0:
            return 0
        
        return 1