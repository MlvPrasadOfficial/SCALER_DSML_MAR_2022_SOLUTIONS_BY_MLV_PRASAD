class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        arr = A
        n = len(arr)

        sums = 0

        for i in range(0, n):

            # Xor all the elements of the array
            # all the elements occurring twice will
            # cancel out each other remaining
            # two unique numbers will be xored
            sums = (sums ^ arr[i])

        # Bitwise & the sum with it's 2's Complement
        # Bitwise & will give us the sum containing
        # only the rightmost set bit
        sums = (sums & -sums)

        # sum1 and sum2 will contains 2 unique
        # elements initialized with 0 box
        # number xored with 0 is number itself
        sum1 = 0
        sum2 = 0
        zz=[]

        # Traversing the array again
        for i in range(0, len(arr)):

            # Bitwise & the arr[i] with the sum
            # Two possibilities either result == 0
            # or result > 0
            if (arr[i] & sums) > 0:

                # If result > 0 then arr[i] xored
                # with the sum1
                sum1 = (sum1 ^ arr[i])
                zz.append(sum1)

            else:

                # If result == 0 then arr[i]
                # xored with sum2
                sum2 = (sum2 ^ arr[i])
        # zz.append(sum1)
        # zz.append(sum2)
        aaa = [sum1,sum2]
        aaa = sorted(aaa)
        # zz = [sum2,sum1]
        return aaa

        # Print the the two unique numbers
        # print("The non-repeating elements are ",
        #     sum1, " and ", sum2)


    # Driver Code
    