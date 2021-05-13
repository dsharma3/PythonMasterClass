class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14
    
    def getArea(self):
        return (self.radius**2) * self.pi
    def __str__(self):
        return "This is circle with radius {}".format(self.radius)
    def __len__(self):
        return self.radius*4
    def __hash__(self):
        return self.radius * 1201212
    def __eq__(self, value):
        return hash(self) == hash(value)
circle = Circle(3)
circle2 = Circle(3)

print(circle.__eq__(circle2))

print(hash(circle))
print(hash(circle2))

# a = 123
# b = 123
# print(hash(a))
# print(hash(b))
# print(a==b)