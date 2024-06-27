# Without using recursive function
# While loop
# use chatGPT to understand

def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits+= n % 10 # remainder
        n = n // 10 # quotient
        # / - div
        # // - Quotient
        # % - Remainder
    return sum_digits

print(sum_of_digits(12345)) # 15



# use of *
# ** karws - can be done
def prepare_pizza(*topings, bases):
    print(topings, bases)

   # pizza = prepare_pizza(*topings:"tomato", "paneer", bases = "thick_crust")
