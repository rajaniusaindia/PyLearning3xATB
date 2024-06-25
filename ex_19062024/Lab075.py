# Lamda expression - do the task in 1 line

def double_my_salary(salary):
    return salary * 2

new_salary = double_my_salary(100)
print(new_salary)

# salary = 100 not correct
# use lambda expression 1 line - use lambda variable, salary, return type
f_double = lambda salary: salary * 2
print(f_double(100))
