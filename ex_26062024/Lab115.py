# Another example with - Constructor
# no new keyword like java
class Dog:
    # every class should have some starting poitn - number initialized
    name = None
    id = None

    # Call function automatically - __init__ =>
    # private in nature only avbl in class
    # Class(0 name in Java, this.class
    def __init__(self, name, id):
        # Dog.__init__() missing 2 required positional arguments: 'name' and 'id'
        self.name = name
        self.id = id

    # Constructor ?
    # Use to initialize the values
    # of the instance variable (attributes)

    def sleep(self):
        print("Sleeping")

dog1 = Dog()
print(dog1) # <__main__.Dog object at 0x101e5baa0>
print(dog1.name)
dog1.name = "Chow"
print(dog1.name) # Chow
dog1.sleep()

dog2 = Dog()
print(dog2) # <__main__.Dog object at 0x101e5ba70>

# again I have to do
print(dog2.name)
dog2.name = "Mow"
print(dog2.name) # Chow
dog2.sleep()

# Call function automatically - __init__ =>
# private in nature only avbl in class