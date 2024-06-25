# List - collection of items
# Is mutable
# Can store duplicate items
# any data type
# very important - to be used in API
my_list = [1,2,3,1,2,3]
print(my_list)
my_list2 = [1,2,'True', 10.00]
print(my_list2)

# Indexing
print(my_list[0])
print(my_list[3])

my_list[1] = 20
print("List after changing element at index 1:", my_list)

# append - add in the end
my_list.append(4)
print(my_list)

# extend
my_list.extend([5,6])
print(my_list)

# insert
my_list.insert(1, 'a')
print(my_list)

# remove
my_list.remove('a')
print(my_list)

# copy
# Shallow vs deep later
my_copy_list = my_list.copy()
print(my_copy_list)

# clear after making a copy - see above
my_list.clear()
print("Initial list: ", my_list)
print(my_copy_list)

# delete


# index[3] - throw error
# my_list("Index of 3 in the list:", my_list(3))

# sort the list
my_copy_list.sort()
print(my_copy_list)

# Shallow copy of list

# Soft copy of list

# reverse list
my_copy_list.reverse()
print(my_copy_list)


# different types of elements  -  not supported

# check if loop = if not squares print empty else
