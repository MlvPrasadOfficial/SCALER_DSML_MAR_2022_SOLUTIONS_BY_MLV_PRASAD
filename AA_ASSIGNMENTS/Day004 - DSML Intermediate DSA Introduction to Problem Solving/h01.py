def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = int(input())
    if a > 0 :        
        print("1")  
    
    for a in range(10,a+1) :
        # n = 3 #len(str(a))
        temp = a
        sum1 = 0
        
        while (temp != 0):
            r = temp % 10
            sum1 = sum1 + (r**3)
            temp = temp // 10
        
    # If condition satisfies
        if sum1 == a :
            print(sum1)
        

        



if __name__ == '__main__':

    main()