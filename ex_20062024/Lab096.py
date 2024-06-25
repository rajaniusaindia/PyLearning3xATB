# decorators
# a function that takes another function as an argument and return a new function
# extending or changing its behavior

# example - iphone and a cover for a iphone is a decorator

def my_decorator(func):
    def wrapper():
        print("Starting....")
        print("************")
        func()
        print("************")
        print("Ending....")

    return wrapper()

# Decorator Annotation
@my_decorator
def say_hello():
    print("Say Hello")
# say_hello - automatically called
# output
# Starting....
# ************
# Say Hello
# ************
# Ending....

# not callable - no need to register with JetBrains


