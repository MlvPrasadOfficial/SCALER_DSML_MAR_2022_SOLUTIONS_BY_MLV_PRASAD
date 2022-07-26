class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        x_count=0
        y_count=0
        x=0
        y=0
        n=len(A)
        for a in A:
            if a==x:
                x_count=x_count+1
            elif a==y:
                y_count=y_count+1
            elif x_count==0:
                x=a
                x_count=x_count+1
            elif y_count==0:
                y=a
                y_count=y_count+1
            else:
                x_count=x_count-1
                y_count=y_count-1        
        count_x=0
        count_y=0
        for a in A:
            if a==x:
                count_x=count_x+1
            elif a==y:
                count_y=count_y+1
        if count_x>n/3:
            return x
        if count_y>n/3:
            return y
      
        return -1