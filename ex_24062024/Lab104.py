# Filter in Python - built-in function
# allows to filter the elements in a - list, tuple and
# filter always works with function - 1st argument is always a function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter the above - even items
new_list_even = [2, 4, 6, 8]


def is_even(num):
    return num % 2 == 0


def is_greater_5(num):
    return num > 5


new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))

# do not use the same function name - it will throw an error
num_greater_5 = filter(is_greater_5, numbers)
print(list(num_greater_5))

# if true will be in the list or else - False not taken in the list
