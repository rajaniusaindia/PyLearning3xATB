# Smaller functions can be converted into lambda functions - 1 liners
# lambda arguments: expression - hard to understand initially but very useful
# try it until you become comfortable

# new - python thing - goes away
# Even odd number - 1 liner

def find_odd_even(num):
    if (num % 2 == 0):
        print("Even")
    else:
        print("Odd")
# print(find_odd_even(10))
# print(find_odd_even(11))

# convert to 1 line lambda expression
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(10))
print(check_even_odd(11))
