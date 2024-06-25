# double numbers in a list
# [2, 4, 6, 8, 10] => [1, 2, 3, 4, 5]
my_list = [1, 2, 3, 4, 5]  # do not use - list keyword gets confused
print(my_list * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# not correct

# use loop
# use temp list - always create a new temp list to store the double values
temp_list = []
for i in my_list:
    # both will work
    temp_list = i * 2
    # temp_list.append(i * 2)
print(temp_list)  # [2, 4, 6, 8, 10]


# lambda expression
# can we do it without a temp_list
# yes  create a function
def double_item(num):
    return num * 2

# can also use lambda
# double_item = lambda num:num**2

# map() is a function
# 1. take each item from the list - pick o1 item at a time
# 2. execute the function on it
# 3. return same number of elements (list)

# Without using any for loop - powerful cool
# will return map object
double_list = map(double_item, my_list)

# Need to convert to List object
double_list = list(map(double_item, my_list))
print(double_list)  # [2, 4, 6, 8, 10]

# We can use lambda to further reduce it to 1 line code
# Good Practice not to have 1 liner for others to understand code
