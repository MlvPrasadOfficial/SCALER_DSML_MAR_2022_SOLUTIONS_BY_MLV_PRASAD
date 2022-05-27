class Solution:

        
    def LCM(self, A, B):
        def gcd(a,b):
            if a == 0:
                return b
            return gcd(b % a, a)
        return int((A / gcd(A,B))* B)
        
#    a x b = LCM(a, b) * GCD (a, b)

#    LCM(a, b) = (a x b) / GCD(a, b)
