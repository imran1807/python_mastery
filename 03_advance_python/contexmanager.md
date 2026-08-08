# 📂 Context Managers in Python

> A complete guide to Python Context Managers (`with` statement), resource management, custom context managers, and best practices with practical examples.

---

# 📖 Table of Contents

1. Introduction
2. Why Context Managers?
3. Traditional Resource Management
4. The `with` Statement
5. How `with` Works
6. The `__enter__()` Method
7. The `__exit__()` Method
8. Exception Handling
9. Returning Values with `__enter__()`
10. Suppressing Exceptions
11. Creating Custom Context Managers
12. Real-World Applications
13. Best Practices
14. Common Mistakes
15. Interview Questions
16. Summary

---

# 1️⃣ Introduction

A **Context Manager** is an object that automatically manages resources such as:

- Files
- Database Connections
- Network Connections
- Locks
- GPU Resources

It ensures resources are properly acquired and released, even if an exception occurs.

---

# 2️⃣ Why Context Managers?

Without a context manager:

```python
file = open("sample.txt", "r")

data = file.read()

file.close()
```

This works only if no error occurs.

Suppose:

```python
file = open("sample.txt", "r")

print(10 / 0)

file.close()
```

Output

```
ZeroDivisionError
```

The file never closes.

This causes a **resource leak**.

---

# 3️⃣ Traditional Resource Management

Before context managers, we used:

```python
file = open("sample.txt")

try:
    data = file.read()

finally:
    file.close()
```

The `finally` block always executes.

Although correct, this approach becomes repetitive.

---

# 4️⃣ The `with` Statement

Python provides a cleaner solution.

```python
with open("sample.txt", "r") as file:
    data = file.read()
```

Python automatically:

```
Open Resource
      ↓
Execute Block
      ↓
Close Resource
```

No explicit `close()` call is required.

---

# 5️⃣ How `with` Works

A context manager implements two special methods:

```python
__enter__()
```

and

```python
__exit__()
```

Internally,

```python
with Resource():
    print("Working")
```

is similar to

```python
obj = Resource()

obj.__enter__()

try:
    print("Working")

finally:
    obj.__exit__()
```

---

# 6️⃣ The `__enter__()` Method

Executed when entering the `with` block.

Example

```python
class Resource:

    def __enter__(self):
        print("Resource Acquired")
```

Output

```
Resource Acquired
```

---

# 7️⃣ The `__exit__()` Method

Executed when leaving the `with` block.

```python
class Resource:

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource Released")
```

Output

```
Resource Released
```

This method executes even if an exception occurs.

---

# 8️⃣ Exception Handling

Example

```python
class Demo:

    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")

with Demo():
    print(10 / 0)
```

Output

```
Enter
Exit
Traceback...
```

Notice

`__exit__()` executes before the exception is propagated.

---

# 9️⃣ Returning Values from `__enter__()`

Whatever `__enter__()` returns is assigned after `as`.

```python
class Database:

    def __enter__(self):
        return "Database Connected"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnected")
```

Usage

```python
with Database() as db:
    print(db)
```

Output

```
Database Connected
Disconnected
```

---

# 🔟 Parameters of `__exit__()`

```python
def __exit__(self, exc_type, exc_value, traceback):
```

### `exc_type`

Type of exception

Example

```
ZeroDivisionError
```

---

### `exc_value`

Actual error message

```
division by zero
```

---

### `traceback`

Contains stack trace information.

Useful for debugging.

If no exception occurs,

all three values are

```python
None
```

---

# 1️⃣1️⃣ Suppressing Exceptions

Returning

```python
return True
```

inside `__exit__()`

tells Python

> "The exception has been handled."

Example

```python
class Demo:

    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Handled")
        return True

with Demo():
    print(10 / 0)

print("Program Continues")
```

Output

```
Start
Handled
Program Continues
```

The program does not crash.

---

# 1️⃣2️⃣ Creating a Custom Context Manager

```python
class MyContext:

    def __enter__(self):
        print("Entering")
        return "Python"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving")
```

Usage

```python
with MyContext() as text:
    print(text)
```

Output

```
Entering
Python
Leaving
```

---

# 1️⃣3️⃣ Real-World Applications

Context managers are widely used in:

### File Handling

```python
with open(...)
```

---

### Database Connections

```python
with sqlite3.connect(...)
```

---

### Thread Locks

```python
with lock:
```

---

### Machine Learning

```python
with torch.no_grad():
```

---

### Network Sessions

```python
with requests.Session():
```

---

# 1️⃣4️⃣ Best Practices

✔ Always use `with` when working with files.

✔ Keep `__enter__()` lightweight.

✔ Release resources in `__exit__()`.

✔ Handle exceptions only when appropriate.

✔ Return `True` only if you intentionally want to suppress exceptions.

---

# 1️⃣5️⃣ Common Mistakes

❌ Forgetting to release resources.

```python
file = open(...)
```

without

```python
close()
```

---

❌ Returning `True` accidentally.

This may hide important errors.

---

❌ Doing heavy work inside `__enter__()`.

Acquire only the required resources.

---

# 1️⃣6️⃣ Interview Questions

### Q1. What is a Context Manager?

### Q2. Why do we use the `with` statement?

### Q3. Difference between `try-finally` and `with`?

### Q4. What does `__enter__()` do?

### Q5. What does `__exit__()` do?

### Q6. What happens if an exception occurs inside a `with` block?

### Q7. What happens if `__exit__()` returns `True`?

### Q8. What is assigned after the `as` keyword?

---

# 📚 Summary

✔ Context Managers

✔ Resource Management

✔ `with` Statement

✔ `__enter__()`

✔ `__exit__()`

✔ Exception Handling

✔ Returning Values

✔ Suppressing Exceptions

✔ Custom Context Managers

✔ Real-World Applications

---

# 🎯 Key Takeaways

- Context Managers automatically manage resources.
- `with` is cleaner and safer than `try-finally`.
- `__enter__()` acquires resources.
- `__exit__()` releases resources.
- Exceptions do not prevent cleanup.
- Returning `True` suppresses exceptions.
- Context Managers are widely used in file handling, databases, networking, and AI frameworks like PyTorch.

---

⭐ If you found this helpful, consider starring the repository!