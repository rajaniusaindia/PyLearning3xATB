# Dictionary - key value pair
# name => key=Name value=Pramod
# Unordered collection of key value pairs
# mutable and change value

my_dict = {}
my_dict = {"name": "Pramod",
           "age": 45,
           "address": "Bangalore"
           }
print(len(my_dict))
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["address"])

# no double quote if use - keyword - dict
phone_book = dict(name="Amit", age=45, address="Delhi")
print(phone_book)
# {'name': 'Amit', 'age': 45, 'address': 'Delhi'}

# can we change name - yes
my_dict["name"] = "Sashi"
print(my_dict)

# tuple is the only one - change not allowed


