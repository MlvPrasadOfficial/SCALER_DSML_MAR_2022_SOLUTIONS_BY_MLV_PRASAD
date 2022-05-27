from collections import deque
class Solution:

    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        C = deque(A)
        D= deque(B)
        count = 0
        for i in range(len(A)):
            # print(C,"D",D)
            k = D[0]
            l = C.index(k)
            # print(k,l)
            C.rotate(-l)
# #             print(C)
            C.popleft()
            D.popleft()
            count += 1 +l

            if C == D :
                count+= len(C)
                break
        return count