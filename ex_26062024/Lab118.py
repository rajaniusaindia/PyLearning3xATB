# Ctr - rules When to create ctr
class Calc:
 # You can create default constructor
 # It will run on its own
 # Create ctr only when you need to assign values,
 # run a special method while creating an object

    # def __init__(self):
    #     print("Hello DC")

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Hello DC => " + str(a) + str(b))

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

# IF using ctr => give args here
object_ref = Calc(2,3)# When you run the program, CTR will run automatically.

# if not using ctr, no args needed, only use function - object already initialized via ctr
output1 = object_ref.sum()
print(output1)
output2 = object_ref.mul()
print(output2)

