
class Solution:
    def solve(self, A):
        ################
        def check(x, A):
            ct = 0
            for a in A:
                if (a & x) == x:
                    ct += 1
            if ct > 3:
                return 1
            return 0
        #################

        ans = 0
        for i in range(32, -1, -1):
            temp = ans | (1 << i)

            if check(temp, A) == 1:

                ans = temp

        return ans