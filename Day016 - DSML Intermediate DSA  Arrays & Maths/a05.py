class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # ans = 0
        # x = 1
        # while(A > 0):
        #     x = x*5
        #     if(A%2 == 1):
        #         ans += x
        #     A = A//2
        # return ans

        n = A
        arr = []
        while n  > 0 :
            r = n %2
            arr.append(r)
            n //= 2
        arr = arr[::-1]

        summ = 0
        aaa=[]
        for i in range(len(arr)):          
            if arr[i] == 1:
                aaa.append(i)
                summ += 5**(len(arr)-i)
        return summ
