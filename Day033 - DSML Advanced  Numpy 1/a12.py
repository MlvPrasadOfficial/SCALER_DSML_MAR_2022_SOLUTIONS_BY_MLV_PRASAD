import numpy as np

def binary(arr):

    """
        function take input array and return output array of binary representation of each element 
    """
    #YOUR CODE GOES HERE
    def func(x):
        ls=""
        while x>0:
            ls = ls+ str(x%2)
            x=x//2 
        return int(ls[::-1])
    vec= np.vectorize(func)
    arr= vec(arr)
    return arr