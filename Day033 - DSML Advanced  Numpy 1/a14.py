# import numpy as np
# def countfreq(arr2d):
#     # Make sure that you are printing the output matrix simply inside this function.
#     '''input: arr2d= a 2d python list
#         output: a 2d numpy array'''
#     r = len(arr2d)
#     c = len(arr2d[0]) 
#     l =[]


#     for i in range(r) :
#         count1 = 0
#         count2 = 0
#         count3 = 0
#         count4 = 0
#         count5 = 0
#         count6 = 0
#         count7 = 0
#         count8 = 0
#         count9 = 0
#         count9 = 0
#         count10 = 0
#         for j in range(c):
#             if arr2d[i][j] == 1 :
#                 count1 += 1
#             elif arr2d[i][j] == 2 :
#                 count2 += 1
#             elif arr2d[i][j] == 3 :
#                 count3+= 1
#             elif arr2d[i][j] == 4 :
#                 count4+= 1
#             elif arr2d[i][j] == 5 :
#                 count5+= 1
#             elif arr2d[i][j] == 6 :
#                 count6+= 1
#             elif arr2d[i][j] == 7 :
#                 count7+= 1
#             elif arr2d[i][j] == 8 :
#                 count8+= 1
#             elif arr2d[i][j] == 9 :
#                 count9+= 1
#             elif arr2d[i][j] == 10 :
#                 count10+= 1
#         if j == 0:
#             l[i][j] = count1
#         if j == 1:
#             l[i][j] = count2
#         if j == 2:
#             l[i][j] = count3
#         if j == 0:
#             l[i][j] = count4
#         if j == 0:
#             l[i][j] = count5
#         if j == 0:
#             l[i][j] = count6
#         if j == 0:
#             l[i][j] = count7
#         if j == 0:
#             l[i][j] = count8
#         if j == 0:
#             l[i][j] = count9
#         if j == 0:
#             l[i][j] = count10
#         l.append([count1,count2,count3,count4,count5,count6,count7,count8,count9,count10])  
#     return np.array(l)
import numpy as np
def func(row):
    uniq, count = np.unique(row, return_counts=True)
    zeros = np.zeros(10)
    zeros[uniq-1] = count
    return (zeros.astype(int))


def countfreq(arr2d):
    # YOUR CODE GOES HERE
    # No need to write code to take input
    
    return np.array([func(row) for row in arr2d])