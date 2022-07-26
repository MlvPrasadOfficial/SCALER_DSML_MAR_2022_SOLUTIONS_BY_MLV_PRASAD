# function to check whether characters 
# of a string can form a palindrome  
def canFormPalindrome(st) : 
  
    # Create a count array and initialize   
    # all values as 0 
    count = [0] * (26) 
  
    # For each character in input strings, 
    # increment count in the corresponding 
    # count array 
    for i in range( 0, len(st)) : 
        count[ord(st[i])-ord('a')] = count[ord(st[i])-ord('a')] + 1
  
    # Count odd occurring characters 
    odd = 0
      
    for i in range(0, 26) : 
        if (count[i] & 1) : 
            odd = odd + 1
  
        if (odd > 1) : 
            return False
              
    # Return true if odd count is 0 or 1,  
    return True
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if(canFormPalindrome(A)):
            return 1
        return 0
