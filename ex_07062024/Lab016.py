# take 2 input number from the user and add them
# Type conversion
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# if String will concat so need to do
# type conversion
# int to str => int(str)
# str to number => str(num1)

print(type(num1))
result = num1 + num2

print("The sum is: ", result)

# or better code

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# type converstion from str -> int
result = int(num1) + int(num2)
print("The sum is: ", result)
print(type(result))

# typr conversion from int -> str
result = str(result)
print(result)
print(type(result))


