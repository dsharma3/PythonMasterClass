class Animal():
    def __init__(self):
        print("Animal created")
    
    def whoami(self):
        print("I am an Animal")

    def eat(self):
        print("eating")

# animal= Animal()
# animal.whoami()
# animal.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    
    def eat(self):
        print("Dog eating")
dog1 = Dog()
dog1.whoami()
dog1.eat()