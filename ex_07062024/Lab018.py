# Funny things supported in Python
# Raw String
# Format the String

# ' ', " ", """
name = 'Rajani'
print(name)

name1 = "Pramod"
print(name1)

name2 = """Rajani"""
print(name2)

name = "John"
age = 20
print(f"Hello {name}, you are {age} years old.")

# case of /n - newline
# Python - cannot use escape character
# Java we can handle by double quotes
# dir = "C:\nomedir\some_dir"

# Python use - raw - r and single quotes to handle this
dir = r'C:\nomedir\some_dir'

dir = r'C:\nomedir\some_dir'
print(dir)

# f -> formatting - it will replace the values of the variables
# {} -> placeholder - it will replace the values of the variables

first_name = "Rajani"
last_name = "Choudhary"

print(first_name + " " + last_name)
print(first_name, last_name)

# use - f to format
print(f'Your full name is {first_name} {last_name}' )
