# tuple - collection of Items tuple () = immutable - cannot change the values
# Similar to List [] = mutable - value can be but tuple value cannot be changed
# both can store duplicates
# do not use list as a variable name - list is a keyword

my_list = [1, 2, 3, 4, 2, 4] # modify the list
my_list[2] = 6
print(my_list)  # [1, 2, 6, 4]
print(id(my_list))

# () brakets    vs List []
my_tuple = (1, 2, 3, 4, 2, 4)
print(my_tuple)

# cannot change value like list
# my_tuple[2] = 6 # TypeError: 'tuple' object does not support item assignment
print(my_tuple)
print(id(my_tuple))