# class, methods, objects
# Blue-print of a class
class Person:
    # attributes
    name = None
    id = None
    age = None
    phone_number_ = None

    # Behavior
    def talk(self): # no arg => No return
        print("I can talk")

    def sleep1(self): # arg => no return
        print("I am a method")

    def sleep2(self, name): # arg => withreturn
        print("I am a method")
        # print("Sleep", name)
        return None

    # Normal function
    def walk(self):
        print("I can walk")

    def walk_return(self): # no arg => with return
        return("I can walking..")


# create an object of the Person class
# a new memory location - to store attributes
# Different memory, different methods also
surya = Person()
surya.name = "Surya Prakash"
print(surya.name)
surya.talk()

# a new memory location - to store attributes
# Object referece = Object - ClassName()
ritika = Person()
ritika.name = "Ritika Gupta"
print(ritika.name)
ritika.walk()
