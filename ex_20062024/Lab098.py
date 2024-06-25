# 2 Decorators
def decorator1(func):
    def wrapper():
        print("Decorator 1 ")
        func()
        return wrapper()

def decorator2(func):
    def wrapper():
        print("Decorator 1 ")
        func()
        return wrapper()

@decorator1
@decorator2
def say_hello():
    print("Hello")


