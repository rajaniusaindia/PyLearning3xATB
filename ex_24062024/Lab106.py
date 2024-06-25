# Filter different from Map() - huge difference
# n = n + 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double_me(num):
    return num * 2


# use lambda
# double_me_lambda = lambda n: n * 2
# map - pick one item and apply function to each item - get same number of items
# new_map = list(map(double_me, numbers))
# or call lambda function
# new_map = list(map(double_me_lambda, numbers))
# or can directly use lambda

new_map = list(map(lambda n: n * 2, numbers))
print(new_map)


# filter - pick item m, if true keep it, false - remove it - less number of items
# only works when it is true
def even_numbers(num):
    return num % 2 == 0


# new_filter_list = list(filter(even_numbers, numbers))
# or use lambda directly here
new_filter_list = list(filter(lambda num: num % 2 == 0, numbers))
print(new_filter_list)
