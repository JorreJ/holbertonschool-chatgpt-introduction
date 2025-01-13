#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Please enter an integer")
            sys.exit(1)
        
        num = int(sys.argv[1])
        
        if num < 0:
            print("Factorial is not defined for negative number")
            sys.exit(1)

        f = factorial(int(sys.argv[1]))
        print(f)

    except ValueError:
        print("Please enter a valid integer")
        sys.exit(1)