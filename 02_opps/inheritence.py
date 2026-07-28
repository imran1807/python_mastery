"""class Animal:
    def eat(self):
        print("its eating")
    def sleep(self):
        print("its sleeping")

class Dog(Animal):
    def bark(self):
        print("bow bow")
class Vehicle:
    def start(self):
        print("Vehicle Started")
class Car(Vehicle):
    def start(self):
        super().start()
        print("Car Ready to Drive")
"""
class Person:
    def walk(self):
        print("the person is walking")
class Student(Person):
    def Study(self):
        print("the student is studying")
class Engieering_student(Student):
    def code(self):
        print("he is coding")
class shape:
    def display(self):
        print("called the shape")
class triangle(shape):
    def draw_triangle(self):
        print("triangle is drawned")
class circle(shape):
    def draw_circle(self):
        print("circle is drawned")
class square(shape):
    def draw_square(self):
        print("square is drawned")





if __name__=="__main__":
    """imran=Engieering_student()
    print(imran.walk())
    print(imran.code())
    print(imran.Study())"""
    triangle1=triangle()
    shape1=shape()
    triangle1.draw_triangle()
    triangle1.display()
    shape1.display()
    

    