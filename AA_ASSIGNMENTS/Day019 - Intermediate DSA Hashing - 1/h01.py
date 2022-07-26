class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self,A, B, C):
        hashmap = {}

        for i in range(len(C)):
            # print(i )
            if hashmap.get(C[i])  == None :
                hashmap[C[i]]   = 1
                # print(hashmap,"0")
            else :
                hashmap[C[i]]  += 1
                # print(hashmap,"9")
        # return hashmap
        zz=[]
        for v ,k in hashmap.items():
            if k == B :
              zz.append(v)
        
        if len(zz) == 0:
            return -1
        else :
            return (sum(zz))

