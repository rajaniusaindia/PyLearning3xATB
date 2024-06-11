Operators

# Assignment operator
name = "Pramod"

# compare operator (bool)
v1 = (1 == True)
v2 = (0 == False)
print(v1)
print(v2)


age = +65 # unary operator - 65 - positive - self explanatory
print(age)

num = -1 # specifically type
print(num)

r = age + num  # BODMAS
print(r)
print(type(r)) # 64 (65+ -1 = 64

# Not Operator - not present in Java - works only with (Boolean)
is_married = True
print(not is_married)

# IS Operator - Identity operator
a = 5
b = 6
c = False

# Where it is used ??  Conditions ?? later
print(a + b)
print(a is b)

my_list = [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list)
print(my_list2)
print(my_list is my_list2) # 2 different Lists - False

