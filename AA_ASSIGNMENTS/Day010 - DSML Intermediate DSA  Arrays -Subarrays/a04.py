class Solution:
    def maxSubarray(self, A, B, C):
        result=[]
        # count = 0
        for i in range(A) :
            res=0
            for j in range(i,(A)):
                res+=C[j]
                if res <= B :
                    result.append(res)
    #                        print(count)
        if len(result) == 0:
            return 0
        else:
            return max(result)
# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : list of integers
#     # @return an integer
#     def maxSubarray(self, A, B, C):
#         ans = 0
#         for i in range(A):
#             sum = 0
#             for j in range(i, A):
#                 sum += C[j]
#                 if (sum <= B):
#                     ans = max(ans, sum)
#                 else:
#                     break
#         return ans
