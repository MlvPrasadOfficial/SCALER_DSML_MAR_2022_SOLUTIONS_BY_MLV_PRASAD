class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        l = len(A)

        minn =[]
        for i in range(len(A)) :
            minn.append(len(A[i]))

        mini = min(minn)
        count = 0

        for j in range(mini):
            ct = 0
            for i in range(len(A)-1):
                if A[i][j] == A[i+1][j] :
                    ct += 1
            if ct == len(A)-1 :
                count +=1
            else :
                break
        
        if count == 0:
            return ""
        else :
            return A[0][:count]