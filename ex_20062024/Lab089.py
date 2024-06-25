# unpacking of the tuple - not used that much
# only learn what will be needed in API automation
a, b, c = (12, 34, 56)

# tupple don't have append so => convert to List and do the operation

t = (12, 34, 56)
# t.append() # tuple are immutable in nature

# How to append if youbreally need
new_t = t + (4,)
print(new_t)

# convert to list and then append to it
my_list = list(t)
print(my_list)
my_list.append(5)


