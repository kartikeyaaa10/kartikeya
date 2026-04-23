class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
length=int(input("Enter length: "))
width=int(input("Enter width: "))
    
    
rect=Rectangle(length, width)
print("area of rectangel :",rect.area())