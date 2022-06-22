def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    k = []
    for i in range(1, n+ 1):
        a = int(input())
        k.append(a)
    
    for j in k :
        zz = []
        for m in range(1,int(j)):
            if int(j)%m == 0:
                zz.append(m) 
        #print(zz)
        if sum(zz)== j:
            print("YES")
        else :
            print("NO")
            #

        
            
    

if __name__ == '__main__':
    main()