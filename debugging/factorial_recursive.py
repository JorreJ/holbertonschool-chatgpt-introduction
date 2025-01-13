#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Function Description:
        This function computes the factorial of a given non-negative integer `n`.
        It uses recursion, where the base case is defined as 0! = 1, and the recursive
        case is defined as n! = n * (n-1)!.

    Parameters:
        n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the input integer `n`. If `n` is 0, the function returns 1.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        # Recursive case: factorial of n is n * factorial of (n-1)
        return n * factorial(n-1)

# Main execution
# `sys.argv[1]` is expected to contain the input number as a command-line argument
f = factorial(int(sys.argv[1]))  # Compute factorial of the input number
print(f)  # Output the computed factorial to the console