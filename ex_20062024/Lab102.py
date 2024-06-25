# Dictionary order is random

my_dict = {'a': 1, 'b': 2, 'c': 35, 'd': 45, 'e': 55}
print(my_dict)
# {'a': 1, 'b': 2, 'c': 35, 'd': 45, 'e': 55}

my_dict = {'b': 1, 'w': 2, 'c': 35, 'd': 45, 'e': 55}
print(my_dict)

# {'b': 1, 'w': 2, 'c': 35, 'd': 45, 'e': 55}

# usually if you run it multiple times it will not keep the same order
# but could not see it here, ideally it should not

# Ordered Collection - can give you order
# keeps the insertion order

from collections import OrderedDict
od = OrderedDict()
od['a'] = 45
od['b'] = 35
od['c'] = 25
od['d'] = 55

print(od)

# OrderedDict([('a', 45), ('b', 35), ('c', 25)])

# For loop - search and find items in a dictionary
my_new_dict = {'a': 1, 'b': 2, 'c': 35}
for k,v in my_new_dict.items():
    # print(k, v)
    if k == 'b':
        print("key with the name b is found")

    op = 'b' in my_new_dict
    print(op)

