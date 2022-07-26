def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    numbers = input().split()
    numbers = list(map(int, numbers)) #######################################
    numbers.pop(0)
    print(max(numbers),min(numbers))
        
  
   
  

if __name__ == '__main__':
    main()