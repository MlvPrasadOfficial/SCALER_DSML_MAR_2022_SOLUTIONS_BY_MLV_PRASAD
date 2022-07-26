class Solution:
    def solve(self,A):
        n = len(A)
        if (n == 1):
            return 1        
        if (n == 2):
            return 0
        sumEven = 0
        sumOdd = 0
        for i in range(n):
            if (i % 2 == 0):
                sumEven += A[i]
            else:
                sumOdd += A[i]
        currOdd = 0
        currEven = A[0]
        res = 0
        newEvenSum = 0
        newOddSum = 0
        for i in range(1, n - 1):
            if (i % 2):
                currOdd += A[i]
                newEvenSum = (currEven + sumOdd -  currOdd)
                newOddSum = (currOdd + sumEven - currEven - A[i])
            else:
                currEven += A[i]
                newOddSum = (currOdd + sumEven -currEven)
                newEvenSum = (currEven + sumOdd -currOdd - A[i])
            if (newEvenSum == newOddSum):
                res += 1
        if (sumOdd == sumEven - A[0]):
            res += 1
        if (n % 2 == 1):
            if (sumOdd == sumEven - A[n - 1]):
                res += 1
        else:
            if (sumEven == sumOdd - A[n - 1]):
                res += 1
        return res



            
        

            
            
                   

        
