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
circle = Circle(3)

print(circle.getArea())
print(len(circle))
mylist=[1,2,3]
# print(len(mylist))
# print(str(mylist))