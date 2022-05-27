class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        index = [0] * 26
        for i in range(len(B)):
            index[ord(B[i]) - 97] = i
        for i in range(len(A)-1):
            word1 = A[i]
            word2 = A[i+1]
            flag = 0
            for k in range(min(len(word1), len(word2))):
                if(word1[k] != word2[k]):
                    if(index[ord(word1[k]) - 97] > index[ord(word2[k]) - 97]):
                        return 0
                    flag = 1
                    break
                
            if(flag == 0):
                if(len(word1) > len(word2)):
                    return 0
                
        return 1