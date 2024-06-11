# Task #2
# Develop a Python script that calculates the square and cube of a given number
# num = 2 sq => 4
# num2 = 3 cube => 8
square = 2**2
print(square)
cube = 2**3
print(cube)

# Create a program that takes 2 numbers as input and
# prints the 1st number if it is greater than, less than or equal to the 2nd number
# Like ternary operator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("First number is greater" if num1 > num2 else "First number is less" if num1 < num2 else "First number is equal")

# test run
# False
# 8
# 6
# 4
# 8
# Enter first number: 30
# Enter second number: 20
# First number is greater

# Enter first number: 10
# Enter second number: 10
# First number is equal

# Enter first number: 10
# Enter second number: 20
# First number is less