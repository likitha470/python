class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        print("radius of the circle",3.14*self.radius**2)
    def perimeter(self):
        print("perimeter",2*3.14*self.radius) 

c1=Circle(21)
c1.Area()
c1.perimeter()

