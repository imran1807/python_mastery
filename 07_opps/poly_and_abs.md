# Python OOP - Polymorphism & Abstraction

# Table of Contents
1. Polymorphism
2. Types of Polymorphism
3. Method Overriding
4. Duck Typing
5. Method Overloading in Python
6. *args and **kwargs
7. Operator Overloading
8. Built-in Polymorphism
9. Abstraction
10. Abstract Classes
11. Abstract Methods
12. Encapsulation vs Abstraction
13. Interview Questions
14. Key Takeaways

---

# 1. Polymorphism

## Definition

Polymorphism means **"one interface, many forms."**

The same method name behaves differently depending on the object calling it.

Example:

```python
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Output

```
Bark
Meow
```

---

# 2. Types of Polymorphism

### Runtime Polymorphism

Achieved using **Method Overriding**.

### Compile-Time Polymorphism

Traditional method overloading.

Python does **not** support compile-time method overloading like C++ or Java.

Instead it uses:

- Default arguments
- *args
- **kwargs

---

# 3. Method Overriding

Definition:

A child class provides its own implementation of a parent class method.

Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")
```

```
Dog().sound()
```

Output

```
Bark
```

---

# 4. Duck Typing

"If it walks like a duck and quacks like a duck, treat it as a duck."

Python cares about **behavior**, not the object's type.

Example

```python
class Teacher:

    def work(self):
        print("Teaching")

class Doctor:

    def work(self):
        print("Treating Patients")

def perform(person):
    person.work()

perform(Teacher())
perform(Doctor())
```

Output

```
Teaching
Treating Patients
```

---

# 5. Method Overloading in Python

Python replaces the old method with the latest one.

Example

```python
class Demo:

    def show(self, a):
        print(a)

    def show(self, a, b):
        print(a, b)
```

Only the second method exists.

### Alternative

Use default parameters.

```python
def show(a, b=None):
    if b is None:
        print(a)
    else:
        print(a, b)
```

---

# 6. *args

Allows multiple positional arguments.

Example

```python
def add(*numbers):
    return sum(numbers)

print(add(10,20))
print(add(10,20,30))
```

Output

```
30
60
```

---

# 7. **kwargs

Allows multiple keyword arguments.

Example

```python
def employee(**details):

    for key,value in details.items():
        print(key,value)

employee(name="Alice", age=22)
```

Output

```
name Alice
age 22
```

---

# 8. Operator Overloading

Operators can behave differently for user-defined objects.

### __add__()

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks
```

---

### __eq__()

```python
class Rectangle:

    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def __eq__(self,other):
        return self.length==other.length and self.breadth==other.breadth
```

---

### __str__()

```python
class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __str__(self):
        return f"{self.name} earns ₹{self.salary}"
```

---

# 9. Built-in Polymorphism

Built-in functions work on different object types.

Examples

```python
len("Python")

len([1,2,3])

len((10,20))

len({"a":1})
```

Operator +

```python
10+20

"Hello"+" World"

[1,2]+[3,4]
```

---

# 10. Abstraction

Definition

Abstraction means **hiding implementation details while showing only essential features.**

Example

When driving a car:

- You use the accelerator.
- You don't need to know how the engine works internally.

---

# 11. Abstract Class

Python provides the **abc** module.

```python
from abc import ABC, abstractmethod
```

Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

Cannot create objects.

```
Vehicle()
```

Raises

```
TypeError
```

---

# 12. Concrete Class

A class that implements all abstract methods.

```python
class Bike(Vehicle):

    def start(self):
        print("Bike Starting")
```

Now

```python
b=Bike()

b.start()
```

Output

```
Bike Starting
```

---

# 13. Encapsulation vs Abstraction

| Encapsulation | Abstraction |
|--------------|-------------|
| Hides data | Hides implementation |
| Controls access | Shows only required functionality |
| Uses private variables | Uses abstract classes |
| Focuses on security | Focuses on simplicity |

Example

Encapsulation

```
ATM Balance
```

You cannot access balance directly.

Abstraction

```
ATM Withdraw
```

You press buttons.

You don't know the internal banking process.

---

# 14. Interview Questions

### What is polymorphism?

One interface with multiple implementations.

---

### What is method overriding?

Redefining a parent class method in the child class.

---

### Does Python support method overloading?

No.

Python uses:

- Default arguments
- *args
- **kwargs

---

### What is Duck Typing?

Python checks an object's behavior instead of its type.

---

### What is Operator Overloading?

Changing the behavior of operators for user-defined classes.

---

### Difference between __str__() and __repr__()

__str__()

- User-friendly output

__repr__()

- Developer-friendly representation

---

### What is abstraction?

Hiding implementation details while exposing only necessary functionality.

---

### Which module provides abstraction?

```
abc
```

---

### What is an abstract class?

A class that cannot be instantiated and may contain abstract methods.

---

### Which decorator is used for abstract methods?

```python
@abstractmethod
```

---

### Can we create an object of an abstract class?

No.

Python raises

```
TypeError
```

---

# Key Takeaways

✔ Polymorphism means one interface with many implementations.

✔ Method overriding is runtime polymorphism.

✔ Python does not support traditional method overloading.

✔ Duck typing focuses on behavior, not type.

✔ Operator overloading uses magic methods like __add__(), __eq__(), and __str__().

✔ Abstraction hides implementation details.

✔ Abstract classes are created using the abc module.

✔ @abstractmethod forces child classes to implement required methods.

✔ Abstract classes cannot be instantiated.

✔ Encapsulation protects data, while abstraction simplifies usage.

---

# Revision Checklist

- [ ] Polymorphism
- [ ] Method Overriding
- [ ] Duck Typing
- [ ] Method Overloading
- [ ] *args
- [ ] **kwargs
- [ ] Operator Overloading
- [ ] Built-in Polymorphism
- [ ] Abstraction
- [ ] Abstract Classes
- [ ] @abstractmethod
- [ ] Encapsulation vs Abstraction
- [ ] Interview Questions