def main():
    rows = int(input())
    print("*"*rows)
    for i in range(rows,3,-1 )::
        print("*",end="")
        n = rows - i+1
        while n != (rows-2 ):
            print(" ",end="")
            n = n +1
        print("*",end="")
        print()
    print("**")
    print("*")
if __name__ == '__main__':
    main()