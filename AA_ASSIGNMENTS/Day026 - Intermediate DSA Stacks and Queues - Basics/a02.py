from collections import deque
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        ans = []
        q = deque()
        q.append(1)
        q.append(2)
        q.append(3)
        cnt = 3
        while len(ans) < A:
            x = q.popleft()
            ans.append(x)
            if cnt>=A: continue
            x1 = x * 10 + 1
            x2 = x * 10 + 2
            x3 = x * 10 + 3
            q.append(x1)
            q.append(x2)
            q.append(x3)
            cnt += 3

        return ans