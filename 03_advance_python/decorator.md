# 🎯 Decorators in Python

> A complete guide to Python decorators, closures, higher-order functions, and function wrappers with examples, interview questions, and best practices.

---

# 📖 Table of Contents

1. Introduction
2. First-Class Functions
3. Passing Functions as Arguments
4. Returning Functions
5. Nested Functions
6. Closures
7. What is a Decorator?
8. Creating a Decorator
9. Decorators with Arguments (`*args`, `**kwargs`)
10. Preserving Metadata (`@wraps`)
11. Multiple Decorators
12. Practical Decorators
13. Execution Time Decorator
14. Logging Decorator
15. Exception Handling Decorator
16. Retry Decorator
17. Caching with `lru_cache`
18. Best Practices
19. Common Mistakes
20. Real-World Applications
21. Interview Questions
22. Summary

---

# 1️⃣ Introduction

A **decorator** is a function that **modifies or extends the behavior of another function** without changing its original source code.

Instead of modifying the function directly, decorators wrap the original function and add extra functionality.

Examples:

- Logging
- Authentication
- Timing
- Retry mechanisms
- Exception handling
- Caching

---

# 2️⃣ First-Class Functions

Python treats functions as **first-class objects**.

This means functions can:

- Be stored in variables
- Be passed as arguments
- Be returned from other functions
- Be stored inside lists or dictionaries

Example:

```python
def greet():
    return "Hello"

message = greet

print(message())
```

Output

```
Hello
```

---

# 3️⃣ Passing Functions as Arguments

Functions can be passed just like variables.

```python
def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)
```

Output

```
Hello
```

Notice:

```python
execute(greet)
```

✔ Correct

Not

```python
execute(greet())
```

because that passes the **result**, not the function.

---

# 4️⃣ Returning Functions

Functions can return another function.

```python
def outer():

    def inner():
        print("Python")

    return inner

func = outer()

func()
```

Output

```
Python
```

---

# 5️⃣ Nested Functions

Functions defined inside another function.

```python
def outer():

    def inner():
        print("Inner Function")

    inner()

outer()
```

Output

```
Inner Function
```

---

# 6️⃣ Closures

A **closure** remembers variables from its enclosing scope even after the outer function has finished executing.

```python
def outer(message):

    def inner():
        print(message)

    return inner

hello = outer("Hello")

hello()
```

Output

```
Hello
```

The variable `message` is remembered.

---

# 7️⃣ What is a Decorator?

A decorator wraps another function to add functionality.

Without changing:

```python
def greet():
    print("Hello")
```

we can add logging, timing, authentication, etc.

General syntax:

```python
@decorator
def function():
    pass
```

Equivalent to:

```python
function = decorator(function)
```

---

# 8️⃣ Creating a Decorator

```python
def decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper


@decorator
def greet():
    print("Hello")

greet()
```

Output

```
Before Function
Hello
After Function
```

---

# 9️⃣ Decorators with Arguments

To support any number of arguments:

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper
```

### `*args`

Accepts any number of positional arguments.

```python
def add(*args):
    return sum(args)
```

### `**kwargs`

Accepts any number of keyword arguments.

```python
def employee(**kwargs):

    for key, value in kwargs.items():
        print(key, value)
```

---

# 🔟 Preserving Metadata with `@wraps`

Without `@wraps`

```python
print(greet.__name__)
```

Output

```
wrapper
```

Using

```python
from functools import wraps
```

```python
@wraps(func)
```

preserves:

- Function name
- Docstring
- Metadata

---

# 11️⃣ Multiple Decorators

```python
@star
@dash
def message():
    print("Python")
```

Execution Order

```
star
↓

dash
↓

message
```

Output

```
*****
-----
Python
```

---

# 12️⃣ Practical Decorators

Decorators are commonly used for:

- Logging
- Authentication
- Authorization
- Timing
- Validation
- Exception Handling
- Retry Mechanisms
- Memoization

---

# 13️⃣ Execution Time Decorator

```python
import time
from functools import wraps

def time_it(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution Time: {end-start:.4f} seconds")

        return result

    return wrapper
```

---

# 14️⃣ Logging Decorator

```python
from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Starting {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished {func.__name__}")

        return result

    return wrapper
```

---

# 15️⃣ Exception Handling Decorator

```python
from functools import wraps

def safe_execute(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except Exception as e:
            print(f"Error: {e}")

    return wrapper
```

Usage

```python
@safe_execute
def divide(a, b):
    return a / b

divide(10, 0)
```

Output

```
Error: division by zero
```

---

# 16️⃣ Retry Decorator

```python
from functools import wraps
import time

def retry(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        for attempt in range(3):

            try:
                return func(*args, **kwargs)

            except Exception as e:
                print(f"Attempt {attempt+1} failed")

                time.sleep(1)

        print("All retries failed")

    return wrapper
```

---

# 17️⃣ Caching with `lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)
```

Check cache statistics

```python
print(factorial.cache_info())
```

Example Output

```
CacheInfo(hits=1, misses=6, maxsize=None, currsize=6)
```

---

# 18️⃣ Best Practices

✔ Always use `@wraps`

✔ Keep decorators focused on one responsibility.

✔ Use `*args` and `**kwargs`.

✔ Return the original function's result.

✔ Write reusable decorators.

---

# 19️⃣ Common Mistakes

❌ Calling the function instead of passing it

```python
target=greet()
```

✔ Correct

```python
target=greet
```

---

❌ Forgetting to return the wrapper

```python
return wrapper
```

---

❌ Forgetting to return the original function's result

```python
result = func(*args, **kwargs)

return result
```

---

# 20️⃣ Real-World Applications

Decorators are heavily used in:

- Flask
- Django
- FastAPI
- Authentication
- Logging
- Performance Monitoring
- Retrying API Calls
- Machine Learning Pipelines
- Caching Expensive Computations

---

# 21️⃣ Interview Questions

### Q1. What is a decorator?

### Q2. Why do we use `@wraps`?

### Q3. Difference between `*args` and `**kwargs`?

### Q4. What is a closure?

### Q5. What is memoization?

### Q6. Difference between logging and execution time decorators?

### Q7. Explain `lru_cache`.

### Q8. Difference between exception handling and retry decorators?

---

# 22️⃣ Summary

✔ First-Class Functions

✔ Higher-Order Functions

✔ Nested Functions

✔ Closures

✔ Decorators

✔ `@decorator`

✔ `@wraps`

✔ `*args`

✔ `**kwargs`

✔ Multiple Decorators

✔ Execution Time Decorator

✔ Logging Decorator

✔ Exception Handling Decorator

✔ Retry Decorator

✔ `lru_cache`

---

# 🎯 Key Takeaways

- Decorators extend function behavior without modifying the original function.
- `@wraps` preserves function metadata.
- `*args` and `**kwargs` make decorators reusable.
- Decorators are widely used in production frameworks.
- `lru_cache` improves performance by caching results.
- Practical decorators include logging, timing, retry, and exception handling.

---

⭐ If you found this helpful, consider starring the repository!