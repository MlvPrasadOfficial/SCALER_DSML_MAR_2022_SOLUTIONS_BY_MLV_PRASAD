import numpy as np
def sort_marks(arr2d, j):
    '''Input: arr2d= a 2d python list.
              j= integer representing the number of quiz according to which the marks need to be sorted.
        Output: a 2d numpy array.'''

    # Make sure that you are returning the output matrix simply inside this function.
    a = np.array(arr2d)
    
    return a[a[:, j-1].argsort()]
    # YOUR CODE GOES HERE
    
    

