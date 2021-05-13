from Calculation import * as cc

class GrossSalary():
    def __init__(self, salary, tax_rate):
        self.salary = salary
        self.tax_rate = tax_rate
    
    def calculate(self):
        cal = cc()
        return cal.calculateGrossSalary(self.salary, self.tax_rate)


g = GrossSalary(100000,.3)
print(g.calculate())