# 1. Using for loop, write and run a Python program for this algorithm.
# Here is an algorithm to print out n! from 0! to 10!

def calculate_factorials():
    for n in range(11):
        if n == 0:
            factorial = 1
        else:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
        print(f"{n}! = {factorial}")

calculate_factorials()
