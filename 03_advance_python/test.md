# 🧪 Testing in Python (unittest & pytest)

> A complete guide to Python Testing using **unittest** and **pytest**, including assertions, test cases, test discovery, best practices, and interview questions.

---

# 📖 Table of Contents

1. Introduction
2. Why Testing?
3. Types of Testing
4. Unit Testing
5. unittest Framework
6. Writing Your First Test
7. Assertions
8. Testing Exceptions
9. Test Discovery
10. pytest
11. unittest vs pytest
12. Best Practices
13. Common Mistakes
14. Real-World Applications
15. Interview Questions
16. Summary
17. Cheat Sheet

---

# 1️⃣ Introduction

Testing is the process of verifying that your program behaves as expected.

Instead of manually checking every feature after making changes, automated tests verify that existing functionality still works.

Benefits:

- Detect bugs early
- Improve code reliability
- Simplify maintenance
- Increase confidence during refactoring
- Support Continuous Integration (CI)

---

# 2️⃣ Why Testing?

Suppose you wrote:

```python
def add(a, b):
    return a + b
```

Later you accidentally change it:

```python
def add(a, b):
    return a - b
```

Without tests, the bug may go unnoticed.

With automated tests:

```
FAILED
```

You immediately know something is wrong.

---

# 3️⃣ Types of Testing

### Unit Testing

Tests one small unit of code (usually one function).

---

### Integration Testing

Tests how multiple components work together.

---

### System Testing

Tests the complete application.

---

### End-to-End Testing

Simulates real user behavior.

Example:

```
Login

↓

Add Product

↓

Checkout

↓

Payment
```

---

# 4️⃣ Unit Testing

A unit test verifies a single function or method.

Example

```python
def square(x):
    return x * x
```

Test

```python
assert square(5) == 25
```

If true

```
PASS
```

Otherwise

```
FAIL
```

---

# 5️⃣ unittest Framework

Python includes the built-in

```python
unittest
```

module.

Import

```python
import unittest
```

Create a test class

```python
class TestMath(unittest.TestCase):
    pass
```

Every test class should inherit from

```python
unittest.TestCase
```

---

# 6️⃣ Writing Your First Test

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3), 5)

if __name__ == "__main__":
    unittest.main()
```

Output

```
.
----------------------------------------------------------------

Ran 1 test

OK
```

---

# 7️⃣ Assertions

Assertions compare expected and actual values.

## assertEqual()

```python
self.assertEqual(5,5)
```

---

## assertNotEqual()

```python
self.assertNotEqual(5,6)
```

---

## assertTrue()

```python
self.assertTrue(10 > 5)
```

---

## assertFalse()

```python
self.assertFalse(5 > 10)
```

---

## assertIsNone()

```python
self.assertIsNone(value)
```

---

## assertIsNotNone()

```python
self.assertIsNotNone(value)
```

---

## assertIn()

```python
self.assertIn("a","apple")
```

---

## assertNotIn()

```python
self.assertNotIn("z","apple")
```

---

# 8️⃣ Testing Exceptions

Sometimes we expect an exception.

Example

```python
with self.assertRaises(ZeroDivisionError):
    10 / 0
```

The test passes only if

```
ZeroDivisionError
```

is raised.

---

# 9️⃣ Test Discovery

Python automatically finds tests.

Rules

- Test files begin with

```
test_
```

Example

```
test_math.py
```

---

Test methods begin with

```
test_
```

Example

```python
def test_add(self):
```

---

Run all tests

```bash
python -m unittest
```

---

# 🔟 pytest

pytest is an external testing framework.

Install

```bash
pip install pytest
```

Example

```python
def add(a,b):
    return a+b

def test_add():
    assert add(2,3)==5
```

Run

```bash
pytest
```

Much shorter than unittest.

---

# 1️⃣1️⃣ unittest vs pytest

| unittest | pytest |
|-----------|---------|
| Built into Python | External package |
| Class-based | Function-based |
| More boilerplate | Cleaner syntax |
| Uses assert methods | Uses normal assert |
| Standard library | Popular in industry |

---

# 1️⃣2️⃣ Best Practices

✔ Write tests for every important function.

✔ Keep tests independent.

✔ Test edge cases.

✔ Use meaningful test names.

✔ Run tests frequently.

✔ Automate testing with CI/CD.

---

# 1️⃣3️⃣ Common Mistakes

## ❌ Forgetting test_

Wrong

```python
def add_test():
```

Correct

```python
def test_add():
```

---

## ❌ One test depending on another

Each test should be independent.

---

## ❌ Testing multiple things in one test

Prefer

```
One Test

↓

One Responsibility
```

---

## ❌ Ignoring edge cases

Test

- Empty lists
- Negative numbers
- Zero
- Large values
- Invalid input

---

# 1️⃣4️⃣ Real-World Applications

Testing is used in

- Web Applications
- AI Projects
- APIs
- Banking Software
- Medical Software
- Embedded Systems
- Cloud Services

Example

AI preprocessing

```python
assert normalize(255)==1

assert normalize(0)==0
```

Before training a model, verify preprocessing is correct.

---

# 1️⃣5️⃣ Interview Questions

### Q1. What is unit testing?

### Q2. Why is testing important?

### Q3. Difference between unittest and pytest?

### Q4. What is assertEqual()?

### Q5. What is assertRaises()?

### Q6. Why must test methods begin with test_?

### Q7. What is test discovery?

### Q8. What is the purpose of CI/CD with testing?

### Q9. When would you use pytest over unittest?

### Q10. What makes a good unit test?

---

# 1️⃣6️⃣ Summary

✔ Unit Testing

✔ unittest

✔ pytest

✔ Assertions

✔ Exception Testing

✔ Test Discovery

✔ Best Practices

✔ Edge Cases

✔ CI/CD

✔ Automated Testing

---

# 1️⃣7️⃣ Cheat Sheet

## Import

```python
import unittest
```

---

## Create Test Class

```python
class TestMath(unittest.TestCase):
```

---

## Equality

```python
self.assertEqual(a,b)
```

---

## Boolean

```python
self.assertTrue(condition)

self.assertFalse(condition)
```

---

## Exception

```python
with self.assertRaises(ValueError):
```

---

## Run Tests

```bash
python -m unittest
```

---

## Install pytest

```bash
pip install pytest
```

---

## Run pytest

```bash
pytest
```

---

# 🎯 Key Takeaways

- Testing ensures your code behaves correctly and helps catch bugs early.
- `unittest` is Python's built-in testing framework, while `pytest` is a popular third-party alternative with a simpler syntax.
- Assertions verify expected outcomes and exception handling.
- Good tests are small, independent, readable, and cover edge cases.
- Automated testing is an essential part of professional software development and AI projects.

---

⭐ If you found this helpful, consider starring the repository!