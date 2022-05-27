def Fibonacci(n): 
    if n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        return Fibonacci(A)
