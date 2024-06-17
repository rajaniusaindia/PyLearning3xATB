def f1(a, b, c):
    return a + b + c
print("End")

result = f1(3, 4, 5)
print(result)
# change the order ok
result1 = f1(b = 3, c = 1, a=5)
result1(f1()) # missing 3 required positional arguments: 'a', 'b', and 'c'
result(f1(2, 3)) # missing 3 required positional arguments: 'a', 'b', and 'c'
print(result1)
