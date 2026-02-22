
"""
This script performs addition of two numbers provided as command-line arguments.
Example:
    python calc.py 10 20
"""
import sys

def add(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python calc.py <number1> <number2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please provide valid numbers.")
        sys.exit(1)
