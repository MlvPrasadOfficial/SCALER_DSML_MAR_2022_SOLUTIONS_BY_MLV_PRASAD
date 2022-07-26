class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        def findProd(A):
            ret = 1
            for a in A:
                ret *= int(a)
            return str(ret)
            
        numbers = dict()
        strA = str(A)
        for a in strA:
            if a in numbers:
                return 0
            else:
                numbers[a] = 1
        n = len(strA)
        for i in range(2, n + 1):
            for j in range(n - i + 1):
                num = strA[j : j + i]
                ret = findProd(num)
                if ret in numbers:
                    return 0
                else:
                    numbers[ret] = 1
        return 1