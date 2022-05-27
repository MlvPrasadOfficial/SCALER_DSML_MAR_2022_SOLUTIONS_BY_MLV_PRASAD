import math
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = int(input())
    #print(int(math.floor(math.sqrt(a)))+1)

    if a == 1 :
        print("NO")
    for i in range(2,int(math.floor(math.sqrt(a)))+1):
        if a % i == 0:
            print("NO")
            break
    print("YES")

if __name__ == '__main__':
    main()