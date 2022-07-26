def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    rows = int(input())
    n = 0
    print("**"*rows)
    for i in range(1,rows ):
        for j in range(2,(rows-i+2)):
            print("*",end="")
        n = -1
        while n != ( i-1 ):
            # print(n)
            print("  ",end="")
            n = n +1
        # n = 0
        for m in range(rows-i-1,-1,-1):
            print("*",end="")
        print()
    for i in range(rows-1,-1,-1 ):
        for j in range(2,(rows-i+2)):
            print("*",end="")
        n = -1
        while n != ( i-1 ):
            # print(n)
            print("  ",end="")
            n = n +1
        # n = 0
        for m in range(rows-i-1,-1,-1):
            print("*",end="")
        print()


if __name__ == '__main__':
    main()