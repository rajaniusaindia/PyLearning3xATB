# List - collection of items
numbers =[1,2,3]
# outer function
# Executiong never starts from the def line,
# goes directly to where the function is called
# if define a function (in memory) and never call - nothing will be executed
def do_something(numbers):
    numbers.append(4)
    print(numbers)
    numbers[0] = 100 # replace 1 -> 100
    return numbers

l = do_something(numbers) # Pass whole List
print(l) # [100, 2, 3, 4]