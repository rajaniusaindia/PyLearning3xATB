# Set - random order
t = ("Rajani", "TheTestAcademy", "Rajani")
print(t) # tuple - ('Rajani', 'TheTestAcademy', 'Rajani')
print(set(t)) # remove dups - {'TheTestAcademy', 'Rajani'}

# Set - Union
set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set) # all the items - {1, 2, 3, 4, 5, 6}

# Set - Intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2) # 4,5 is common
print(my_set) # {4, 5}

# difference
my_set = set1.difference(set2) # 1,2,3 is common different
print(my_set) # {1, 2, 3}
my_set = set2.difference(set1) # 1,2,3 is common different
print(my_set) # {6, 7, 8} # can be random since unordered - {8, 6, 7}

# both very important concepts in Mathematics


