class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @param G : integer
    # @param H : integer
    # @return an integer
    def solve(self, A, B, C, D, E, F, G, H):
    
        if(B>=H or F>=D) :
            return 0
        if(A>=G or E>=C) :
            return 0
    
        return 1