class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a + self.b)
class child(Parent):
    pass
x = child(10,20)
x.add()
