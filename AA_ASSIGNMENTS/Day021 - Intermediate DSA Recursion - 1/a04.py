

import sys
sys.setrecursionlimit(10**6)

def printreverse(S): 
    if len(S) == 0: 
        return
      
    temp = S[0] 
    printreverse(S[1:]) 
    print(temp, end='') 

def main():
    s = input()
    printreverse(s)
    return 0
    
if __name__ == '__main__':
    main()