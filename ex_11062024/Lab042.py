# Multiple Conditions
# Find max of 3 numbers
# num1, num2, num3
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 and num2 > num3 -> num2
# num3 > num1 and num2 > num3 -> num2

num1 = int(input("Enter 1st number\n"))
num2 = int(input("Enter 2nd number\n"))
num3 = int(input("Enter 3rd number\n"))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)