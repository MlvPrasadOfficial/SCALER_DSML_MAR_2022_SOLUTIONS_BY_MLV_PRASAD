class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        hashDict = dict()
        n = len(A)
        #print A, B
        for a in A:
            if a in hashDict:
                hashDict[a] += 1
            else:
                hashDict[a] = 1
        for i in range(n):
            x = A[i]
            if (x - B >= 0 and x - B in hashDict) or (x+B in hashDict):
                if B == 0:
                    if hashDict[x] >= 2:
                        return 1
                else:
                    return 1
            elif x+B in hashDict:
                return 1
            elif x in hashDict:
                del hashDict[x]
        #print hashDict
        return 0