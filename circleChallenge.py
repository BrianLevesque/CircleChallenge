import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return pow(self.radius, 2) * math.pi
    def grow(self):
        self.radius = 2 * self.radius

    def get_radius(self):
        return self.radius
    def __str__(self):
        return f'''        Diameter: {self.calculate_diameter()}
        Circumference: {self.calculate_circumference()}
        Area: {self.calculate_area()}'''


#circ = Circle(int(input("Please enter a radius for the circle:")))
#print(circ)

