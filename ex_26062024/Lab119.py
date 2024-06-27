# Ctr - reduce lines
class Calc:

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
# object_ref only
print(Calc(3, 4).sum())



