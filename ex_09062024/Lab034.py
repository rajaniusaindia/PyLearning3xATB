# Program - Calculate the Area of a circle
# input -> radius
# output -> area
# Data types
# input -> Int or float (go with bigger one)
# output ->
# Formula -> area = pi * radius * radius -> 3.14
# Good for beginners
import math

radius = int(input("Enter radius\n"))
print(math.pi)
area = math.pi*(radius**2)
area2 = math.pi*(math.pow(radius, 2))
print(area)
print(area2)

# One line code
# Good for exeperinced
# (math.pi*(float(int(input("Enter the radius\n"))**2)))
print((3.14*(float(int(input("Enter the radius\n"))**2))))
# Comment import math and use actual value

