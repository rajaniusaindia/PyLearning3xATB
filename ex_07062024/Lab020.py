# format function - just used to showcase the value
b = 1
print(f"{b}x1={b}")

print("2x{}={},{}".format(b, b*2,3))

# Strings - In Built Functions
# Functions -> Repeat a task - use a function
# input, max, min, id(), length, type() print() sum() av()

# String functions
name = "Rajani"
print(name)
print(type(name))
print(id(name)) # memory address where it is stored - random number
print(len(name)) # length of the string - always starts with 1
name = name.upper()
print(name)
name = name.lower()
print(name)
print(name.count('A'))
print(name.count('a'))

# 0,1,2,3,4,5
# r,a,j,a,n,i
print(name[0])
print(name[4])

print(name[6])
# error - String index out of range
# String is immutable in nature - that can't be changed

