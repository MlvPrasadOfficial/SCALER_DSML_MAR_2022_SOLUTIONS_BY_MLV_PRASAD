# Returns count of pairs in arr[0..n-1]  
# with XOR value equals to x. 
def xorPairCount(arr, n, x): 
    result = 0 # Initialize result 
      
    # create empty set that stores the  
    # visiting element of array.  
    s = set() 
    for i in range(0, n): 
          
        # If there exist an element in set s 
        # with XOR equals to x^arr[i], that  
        # means there exist an element such  
        # that the XOR of element with arr[i]   
        # is equal to x, then increment count. 
        if(x ^ arr[i] in s): 
            result = result + 1
              
        # Make element visited 
        s.add(arr[i]) 
    return result 
      
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return xorPairCount(A,len(A),B)