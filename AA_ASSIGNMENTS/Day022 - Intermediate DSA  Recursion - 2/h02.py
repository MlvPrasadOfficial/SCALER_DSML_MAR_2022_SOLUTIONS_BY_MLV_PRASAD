class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        li=[0,1]
        if(A==1):
            return [0,1]
        else:
            st=2
            for j in range(A-1):
                for i in range(len(li)-1,-1,-1):
                    li.append(st+li[i])
                st<<=1
            return li
