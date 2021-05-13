class Employee():
    def __init__(self, id, firstname,lastname,age, gender):
        self.id = id
        self.firstname=firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender    
    
    # def __hash__(self):
    #     tup = (self.id,self.firstname,self.lastname,self.age,self.gender)
    #     print(tup)
    #     return hash(tup)
    # def __eq__(self, value):
    #     return hash(self) == hash(value)

employeea = Employee(100,"Divyesh", "Sharma", "32","M")
employeeb = Employee(100,"Divyesh", "Sharma", "32","M")
print(employeea.__eq(employeeb))
