# Task 2
# 1. Leap year Checker
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 2
# find factorial of a number
num = int(input("Enter a number\n"))

def factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)
    # call function
    result = factorial(num)
    print(f"The factrial of {number} is {result}")


# 3- Fibanaci series
# Program to display the Fibonacci sequence up to n
def fibonacci(n):
    sequence = [0, 1]

    # Generate the remaining terms of the Fibonacci sequence
    n = int(input("Enter the value of n: "))
    for i in range(2, n):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
        print(sequence)
