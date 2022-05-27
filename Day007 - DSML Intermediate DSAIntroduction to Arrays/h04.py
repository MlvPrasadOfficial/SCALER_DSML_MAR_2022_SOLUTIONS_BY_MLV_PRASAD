def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    length = int(input())
    for m in range(length) :
        a = input()
        b = list(map(int ,input().split()))
        odd =[]
        even = []
        for i in range(len(b)) :
            if b[i] % 2 == 1 :
                odd.append(b[i])
            else :
                even.append(b[i])
        for o in range(len(odd)) :
            print(odd[o],end=" ")
        print("")
        for e in range(len(even)) :
            print(even[e],end =" ")
        print("")

if __name__ == '__main__':
    main()