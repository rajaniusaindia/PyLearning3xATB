# Recorsion
# A technique where a function calls itself to solve a problem

# Key Concepts
# base case
# recursive case
# factorial example
# factorial of 5

n =5
# Base Case: if n =1 do nothing
# Recursive Case: rest of the case - > pass 5, next time pass function itself with a number

# When I need to call myself
# again and again
def factorial(n):
    # base  - lowest it can go
    # When will this function end =>
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# recursive case

print(factorial(5))
