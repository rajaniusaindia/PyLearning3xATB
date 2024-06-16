# For loop with range
for counter in range(0, 100):  # 0 - 99
    print(counter)

# Even number
for counter1 in range(0, 101, 2):
    print(counter1)

# Odd number
for counter2 in range(1, 101, 2):
    print(counter2)

# break
for counter3 in range(1, 101):
    if counter3 == 5:
        break
    print(counter3)
