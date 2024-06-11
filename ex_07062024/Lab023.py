# List Data type - Shopping List
# IS a mutable sequence - change the value
# List items - milk, bread, butter, poha
# 1. Add item
# 1. Remove item
# 1. Update item
# 1. View item
# 1. Exit

shopping_list = ["milk","bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

# hard to debug since Python will not give errors

my_list = [1,2,3,4,True, 3.14,"Pramod"]
print(type(my_list)) # <class 'list'>
print(my_list)

# Built-In functions
shopping_list.append("Yogurt") # add item in the end
print(shopping_list)
shopping_list.insert(2,"Chocolate") # add in the middle
print(shopping_list)
shopping_list.pop() # remove last items

shopping_list.reverse() # Reverse list
print(shopping_list)

shopping_list.sort() # sort list
print(shopping_list)

print(shopping_list.index("poha")) # find index of an item





