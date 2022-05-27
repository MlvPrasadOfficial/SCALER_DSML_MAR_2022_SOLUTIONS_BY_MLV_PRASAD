class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        i = j = 0
        list = []
        sum = A[0]
        flag = False

        while j < n and i < n:
            if sum == B:
                flag = True
                break

            elif sum < B:
                if j + 1 == n:
                    break
                j = j + 1
                sum = sum + A[j]

            else:
                if i + 1 == n:
                    break
                i = i + 1
                sum = sum - A[i - 1]

        if flag == False:
            return [-1]

        for k in range(i, j + 1):
            list.append(A[k])

        return list
