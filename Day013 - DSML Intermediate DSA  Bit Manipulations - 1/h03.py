class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ar = []
        while A > 0 :
            r = A %2
            ar.append(r)
            A = A // 2

        arr= [0]*(32-len(ar))  + ar[::-1] #(original array)
        
        arr = arr[::-1] #  reverse array
        
        summ = 0
        for i in range(32):
            aa = arr[i]*(2**(31-i))
            summ += aa 
        return summ