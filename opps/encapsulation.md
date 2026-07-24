# Python OOP - Encapsulation Revision Notes

## What is Encapsulation?

Encapsulation is the process of **bundling data (variables) and methods
(functions)** into a single class while **restricting direct access** to
internal data.

> **Encapsulation = Data + Methods + Data Protection**

------------------------------------------------------------------------

## Why Encapsulation?

Without encapsulation:

``` python
account.balance = -1000
```

The object enters an invalid state.

With encapsulation:

``` text
User -> Deposit/Withdraw -> Validation -> Private Variable
```

------------------------------------------------------------------------

# Access Modifiers

## Public

``` python
self.name = "Nazir"
```

Accessible from anywhere.

## Protected

``` python
self._marks = 95
```

Convention only. Intended for internal use.

## Private

``` python
self.__balance = 5000
```

Uses **Name Mangling**.

------------------------------------------------------------------------

# Name Mangling

Python converts:

``` text
__balance
```

to

``` text
_BankAccount__balance
```

This discourages accidental access.

------------------------------------------------------------------------

# Getter

``` python
def get_balance(self):
    return self.__balance
```

Purpose: - Read private data safely.

------------------------------------------------------------------------

# Setter

``` python
def set_balance(self, balance):
    if balance >= 0:
        self.__balance = balance
```

Purpose: - Validate data before updating.

------------------------------------------------------------------------

# @property

Instead of:

``` python
account.get_balance()
account.set_balance(5000)
```

Use:

``` python
print(account.balance)
account.balance = 5000
```

Getter:

``` python
@property
def balance(self):
    return self.__balance
```

Setter:

``` python
@balance.setter
def balance(self, value):
    if value >= 0:
        self.__balance = value
```

Optional Deleter:

``` python
@balance.deleter
def balance(self):
    del self.__balance
```

------------------------------------------------------------------------

# Getter vs Property

  Getter/Setter    Property
  ---------------- -------------
  get_balance()    balance
  set_balance(x)   balance = x
  Verbose          Pythonic

------------------------------------------------------------------------

# Interview Questions

1.  What is encapsulation?
2.  Difference between public, protected and private members?
3.  What is name mangling?
4.  Why use getters?
5.  Why use setters?
6.  Why is @property preferred?

------------------------------------------------------------------------

# Best Practices

-   Use private variables for sensitive data.
-   Validate inside setters.
-   Prefer @property in Python.
-   Use PascalCase for classes.
-   Use snake_case for methods.

------------------------------------------------------------------------

# Common Mistakes

-   Mixing self.balance and self.\_\_balance
-   Forgetting validation
-   Accessing private variables directly

------------------------------------------------------------------------

# AI/ML Connection

Libraries like scikit-learn encapsulate internal model parameters. You
interact through methods such as:

``` python
model.fit(X_train, y_train)
model.predict(X_test)
```

instead of modifying internal state directly.

------------------------------------------------------------------------

# Revision Checklist

-   Public
-   Protected
-   Private
-   Name Mangling
-   Getter
-   Setter
-   @property
-   @property.setter
-   @property.deleter
