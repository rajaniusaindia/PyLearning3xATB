# docitionary
# cannot have duplicate keys
# cannot use indexing
# but values can be duplicated
my_dict = {"name": "Pramod",
           "age": 45,
           "isMale": True,
           "address": "Bangalore",
           # "age": 45 - cannot have duplicate key
           }
print(my_dict)
print(my_dict.get("name"))
print(my_dict["address"])  # cannot use index - use name of the key
print(my_dict.values())
print(my_dict.keys())

print(len(my_dict))

# convert to list
print(list(my_dict.keys()))
print(list(my_dict.values()))

# For loop
for k,v in my_dict.items():
    print(k,v)

