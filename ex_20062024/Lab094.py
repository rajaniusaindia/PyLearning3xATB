# Set operations - len of a set

set1 = set(["Rajani", "For", "Rajani."])
print(set1) # {'For', 'Rajani'} - remove dup
print(len(set1))

for i in set1:
    print(i)

set1 = set([1,2,3,4,5,6,7,8,9,10,11,12])
print(len(set1)) #12

# remove
set1.remove(5)
print(set1) # {1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12}
print(len(set1)) #11

# Pop - removes the 1st item
set1.pop()
print(set1) # {2, 3, 4, 6, 7, 8, 9, 10, 11, 12} - remove 1

# add
set1.add(20)
print(set1) # {2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 20}