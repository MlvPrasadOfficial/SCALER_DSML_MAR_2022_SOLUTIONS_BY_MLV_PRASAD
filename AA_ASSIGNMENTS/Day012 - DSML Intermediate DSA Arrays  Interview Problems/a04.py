def main():
    A = int(input())
    N = A
    row = 0
    col = 0
    B = [[ 0 for i in range(A)] for j in range((A))]
    x = 1
    # print(N)
    k = N
    
    while N > 0:
        # l to R:
        if (k-N)%2==0:
            for j in range(col, col + A ):
                B[row][j] = x
                x+=1
        else :
            for j in range(col + A-1,col-1,-1):
                # print(j,N)
                B[row][j] = x
                
                x+=1

        
        N = N -1
        row += 1  
    for i in range(len(B)):
        for j in range(len(B)):
            print(B[i][j],end=" ")
        print()

if __name__ == '__main__':
    main()