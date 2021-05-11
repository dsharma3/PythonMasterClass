'''
1) Scope
2) Oop 
    part 1
    classes
    part 2
        attributes
        methods
        method overloading

'''

#LEGB
'''
Local
Enclosing
Global
Built in
'''

class Dog():
    def __init__(self,breed, name):
        self.breed = breed
        self.name = name

    def getBreed(self):
        print(self.breed)
    
    def getName(self):
        print(self.name)

lab = Dog('Labrador','Jimmy')
huskie = Dog('Huskie','Tommy')

lab.getBreed() 
lab.getName()
huskie.getBreed() 
huskie.getName()