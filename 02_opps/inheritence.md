# Python OOP Revision Notes -- Inheritance

## Overview

Inheritance allows one class to acquire the properties and methods of
another class, promoting code reuse and better organization.

## Syntax

``` python
class Parent:
    pass

class Child(Parent):
    pass
```

## Types of Inheritance

### 1. Single Inheritance

One parent → One child.

### 2. Multilevel Inheritance

Grandparent → Parent → Child.

### 3. Hierarchical Inheritance

One parent → Multiple children.

### 4. Multiple Inheritance

One child inherits from more than one parent.

## Method Overriding

A child class provides its own implementation of a method already
defined in the parent.

## super()

-   Calls the **next class in the Method Resolution Order (MRO)**.
-   Useful for extending parent behavior.

Example:

``` python
class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car Ready")
```

## Method Resolution Order (MRO)

Check it using:

``` python
print(ClassName.mro())
```

Example:

``` python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
```

Typical MRO:

    [D, B, C, A, object]

### Golden Rules

-   Python searches methods according to the MRO.
-   Search stops at the first matching method.
-   `super()` follows the MRO, not simply the parent.

## Interview Questions

1.  What is inheritance?
2.  Explain method overriding.
3.  What is multiple inheritance?
4.  What is MRO?
5.  Difference between parent class and child class.
6.  How does `super()` work in Python?

## Best Practices

-   Use PascalCase for class names.
-   Use snake_case for method names.
-   Prefer `super()` over directly calling the parent class.
-   Avoid unnecessary multiple inheritance.

## Revision Checklist

-   [x] Single Inheritance
-   [x] Multilevel Inheritance
-   [x] Hierarchical Inheritance
-   [x] Multiple Inheritance
-   [x] Method Overriding
-   [x] Constructor Inheritance
-   [x] super()
-   [x] MRO
