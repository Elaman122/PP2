class Shape:
    ar = 0  
    def area(self):
        print(self.ar)

class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght

    def area(self):
        print(self.lenght * self.lenght)


a = Shape()
b = Square(3)

a.area()
b.area()