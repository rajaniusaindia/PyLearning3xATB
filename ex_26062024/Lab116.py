# Another example with - Constructor
# no new keyword like java
# Every Constructor haas its own Constructor.
# Constructors have their own name

class Dog:
    # every class should have some starting poitn - number initialized
    # Instance variable
    name = None
    id = None

    # Call function automatically - __init__ =>
    # private in nature only avbl in class
    # Class() name in Java, this.class
    # Constructor is also a method => just a special method
    # Constructor cannot return anything

    # Default will be Passed - if arg=None
    # def __init__(self, name=None, id=None):
    def __init__(self, name, id):
        # Dog.__init__() missing 2 required positional arguments: 'name' and 'id'
        # mandatory to give same number of argument
        # self -> current object

        self.name = name
        self.id = id


    def sleep(self):
        print("Who is sleeping => " + self.name)


dog1 = Dog("Chow", 1)
print(dog1.name, ":", dog1.id)
dog2 = Dog("Mow", 2)
print(dog2.name, ":", dog2.id)

# format
print(f'{dog1.name} has ID {dog1.id}')
dog2 = Dog("Mow", 2)
print(f'{dog2.name} has ID {dog2.id}')

dog1.sleep()
dog2.sleep()
