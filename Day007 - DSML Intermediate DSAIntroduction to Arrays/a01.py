def main():
    
    A = input().split()
   
    N = len(A)
  
    B = int(input())
    B = B % (N-1) # imoortant 
    
    A = A[N-B:N]+A[1:N-B] # see the order
    for i in range(len(A)) :
        print(A[i],end=" ")
if __name__ == '__main__':
    main()