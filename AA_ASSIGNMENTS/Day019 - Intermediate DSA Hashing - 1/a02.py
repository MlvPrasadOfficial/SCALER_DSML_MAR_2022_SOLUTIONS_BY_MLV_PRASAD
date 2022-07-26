class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # Initialize index of first repeating element
        mini = -1    
        # Creates an empty hashset named ump
        ump = {}    
        # Traverse the input array from right to left
        for i in range(n-1, -1, -1):
            # If element is already in hash set, update min
            if (ump.get(A[i]) == None):
                
                ump[A[i]] = 1
            else:   # Else add element to hash set
                mini = i
        
        if(mini == -1):
            return mini
        
        return A[mini]