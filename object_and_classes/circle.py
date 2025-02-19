class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter // 2

    def calculate_circumference(self):
        result = 2 * Circle.__pi * self.radius
        return result

    def calculate_area(self):
        radius_on_second = self.radius * self.radius
        result = Circle.__pi * radius_on_second
        return result

    def calculate_area_of_sector(self, angle):
        result = (angle / 360) * Circle.__pi * self.radius * self.radius
        return result

circle = Circle(10)
angles = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angles):.2f}")