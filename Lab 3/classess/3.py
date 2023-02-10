class Shape:
    are = 0
    def area(self):
        print(self.are)

class Rectangle(Shape):
    def __init__(self, lenght, wight):
        self.lenght = lenght
        self.wight = wight
  
    def area(self):
        print(self.lenght * self.wight)

a = Shape()
b = Rectangle(2, 3)

a.area()
b.area()