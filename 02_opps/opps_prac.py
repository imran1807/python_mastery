class car:
    
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
class laptop:
    
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class employee:
    company = 'google'
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit  
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Subunit: {self.subunit}, Company: {self.company}")
    def increment_salary(self, amount):
        self.salary += amount
        print(f"Salary after increment: {self.salary}")
    

if __name__ == "__main__":
   """ c=car('suzuki','v200',2020)
    d=car('mercedes','c200',2021)
    print(c.brand)

    f=laptop('hp','pavilion',2022)
    print(f.brand)"""
   print(employee.company)
   e1=employee('sachin',10000,'developer')
   """ print(e1.name)
   print(e1.salary)
   print(e1.subunit)
   print(e1.company)
   e1.company='microsoft'
   print(e1.company)"""
   e1.increment_salary(5000)
   employee.display(e1)