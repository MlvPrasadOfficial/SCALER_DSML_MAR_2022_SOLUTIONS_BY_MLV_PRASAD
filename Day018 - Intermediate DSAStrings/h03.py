class Solution:

    # @param A : string

    # @param B : integer

    # @return an integer

    def solve(self, A, B):

        n = len(A)

        arr = [0]*26

        ans = 0

        for i in A:

            arr[ord(i)-97] += 1

            if(arr[ord(i)-97] == 1):

                ans += 1

        arr.sort()

        for i in range(26):

            if(B-arr[i] >= 0 and arr[i] != 0):

                ans -= 1

                B -= arr[i]

        return ans 