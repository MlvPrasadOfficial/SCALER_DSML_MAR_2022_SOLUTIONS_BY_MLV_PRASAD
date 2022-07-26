class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
	    cnt=0
	    dct={}
        for i in range(B):
            if A[i] in dct:
                dct[A[i]]+=1
            else:
                dct[A[i]]=1
                cnt+=1
        ans=[cnt]
        for i in range(B,len(A)):
            if A[i] in dct:
                if dct[A[i]]==0:
                    cnt+=1
                dct[A[i]]+=1
            else:
                dct[A[i]]=1
                cnt+=1
            if dct[A[i-B]]==1:
                cnt-=1
            dct[A[i-B]]-=1
            ans.append(cnt)
        return ans