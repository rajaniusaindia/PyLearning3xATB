# Set - Difference

# Set - Subset - boolean
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
subset = set2.issubset(set1)
print(subset) # False

# other way around
subset = set1.issubset(set2)
print(subset) # True