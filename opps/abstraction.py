"""from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start():
        pass
class bike(Vehicle):
    def start(self):
        print("bike is starting")
class car(Vehicle):
    def start(self):
        print("car is starting")
c1=car()
c1.start()"""
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        perimeter=2*(self.length+self.breadth)
        return perimeter
    def area(self):
        area=self.length*self.breadth
        return area
r1=Rectangle(10,5)
print(r1.area())
print(r1.perimeter())
    