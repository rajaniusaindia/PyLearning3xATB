# Assignment
# Task #1
# Explain the difference between the = operator and the == operator in Python
a = 10  # Assignment operator - assigns a value to a variable, used to initialize
b = 10
print(a == b)  # Equality operator - compares 2 values and return True if equal, False otherwise

# What does the ** operator do in Python and how is it used?
# The ** operator is used as an exponential.
# It raises the number to the power of the exponent.
print(2 ** 3)  # Prints 8

# What does the ^ operator do in Python and in what context it is commonly used for?
# ^ - a bitwise XOR operation on two numbers.
# 1. Get the binary representations of 5 and 3.
# 5 in binary is 0101
# 3 in binary is 0011
# Do the XOR operation on each corresponding bit:
# 0 XOR 0 = 0
# 1 XOR 0 = 1
# 0 XOR 1 = 1
# 1 XOR 1 = 0
# Get the binary result:
# 0101 and 0011 => Result: 0110
# Convert the result back to decimal:
# 0110 in binary is 6 in decimal.

print(5 ^ 3)  # Prints 6
