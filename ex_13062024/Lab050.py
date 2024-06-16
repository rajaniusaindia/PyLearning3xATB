# range can be negative - print in reverse order
for counter in range(10, 0, -1):  # 0 not included 10 included
    print(counter)

    for counter1 in reversed(range(0, 10)):  # 0 included but not 10
        print(counter1)

        # In Python sam can be achieved by 100 ways. Need core only.
