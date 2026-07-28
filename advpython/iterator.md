# Python Advanced - Iterables & Iterators

# Table of Contents

1. Introduction
2. What is an Iterable?
3. What is an Iterator?
4. Difference between Iterable and Iterator
5. iter() Function
6. next() Function
7. StopIteration Exception
8. How for Loop Works Internally
9. Creating a Custom Iterator
10. Iterator Protocol
11. Interview Questions
12. Key Takeaways
13. Revision Checklist

---

# 1. Introduction

Iterators are one of Python's most powerful features.

Every time you use:

- for loop
- range()
- list
- tuple
- string
- dictionary
- set

Python internally uses **iterators**.

Understanding iterators makes learning:

- Generators
- Pandas
- NumPy
- PyTorch DataLoader
- TensorFlow Dataset

much easier.

---

# 2. What is an Iterable?

## Definition

An **iterable** is any object that can be traversed (looped through) one element at a time.

Examples

```python
list
tuple
string
dictionary
set
range
```

Example

```python
numbers = [10,20,30]

for num in numbers:
    print(num)
```

Output

```
10
20
30
```

Example

```python
name = "Python"

for ch in name:
    print(ch)
```

Output

```
P
y
t
h
o
n
```

---

# 3. What is an Iterator?

## Definition

An **iterator** is an object that remembers its current position while traversing an iterable.

It returns one element at a time.

Think of it as a bookmark inside a book.

Example

```python
numbers = [10,20,30]

it = iter(numbers)
```

Now

```
it
```

is an iterator.

---

# 4. Difference between Iterable and Iterator

| Iterable | Iterator |
|----------|----------|
| Collection of elements | Object used to traverse elements |
| Can be converted into iterator | Already an iterator |
| Does not remember current position | Remembers current position |
| Uses iter() | Uses next() |

Examples

Iterable

```python
numbers = [1,2,3]
```

Iterator

```python
it = iter(numbers)
```

---

# 5. iter() Function

## Purpose

Converts an iterable into an iterator.

Syntax

```python
iterator = iter(iterable)
```

Example

```python
numbers = [100,200,300]

it = iter(numbers)
```

---

# 6. next() Function

## Purpose

Returns the next element from an iterator.

Example

```python
numbers = [100,200,300]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

Output

```
100
200
300
```

---

# 7. StopIteration Exception

When there are no more elements,

Python raises

```
StopIteration
```

Example

```python
numbers=[1,2]

it=iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

Output

```
1
2
StopIteration
```

---

# 8. How for Loop Works Internally

When you write

```python
for i in numbers:
    print(i)
```

Python internally performs

```python
it = iter(numbers)

while True:

    try:
        value = next(it)
        print(value)

    except StopIteration:
        break
```

This is why iterators are so important.

---

# 9. Creating a Custom Iterator

Python allows us to create our own iterator using

- __iter__()
- __next__()

Example

```python
class Count:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 5:

            value = self.num
            self.num += 1
            return value

        raise StopIteration
```

Using

```python
c = Count()

for i in c:
    print(i)
```

Output

```
1
2
3
4
5
```

---

# 10. Iterator Protocol

To become an iterator,

a class must implement:

### __iter__()

Returns the iterator object.

Usually

```python
return self
```

---

### __next__()

Returns the next value.

Raises

```python
StopIteration
```

when iteration is complete.

Example

```python
class Example:

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
```

---

# 11. Common Errors

## Forgetting iter()

Wrong

```python
numbers=[1,2,3]

next(numbers)
```

Output

```
TypeError
```

Correct

```python
it=iter(numbers)

next(it)
```

---

## Forgetting StopIteration

Wrong

```python
class Infinite:

    def __iter__(self):
        return self

    def __next__(self):
        return 1
```

This creates an infinite iterator.

---

## Returning self in __next__()

Wrong

```python
def __next__(self):
    return self
```

Always return the next value, not the object itself.

---

# 12. Interview Questions

## What is an iterable?

An object that can be traversed one element at a time.

Examples:

- list
- tuple
- string
- dictionary
- set

---

## What is an iterator?

An object that returns one element at a time while remembering its current position.

---

## Is every iterable an iterator?

No.

Example

```python
numbers=[1,2,3]
```

A list is iterable but not an iterator.

---

## Is every iterator an iterable?

Yes.

Every iterator is also iterable.

---

## Which function converts an iterable into an iterator?

```python
iter()
```

---

## Which function returns the next value?

```python
next()
```

---

## What is StopIteration?

An exception raised when there are no more elements left in an iterator.

---

## Why does __iter__() return self?

Because the object itself acts as the iterator.

---

## What happens if __next__() never raises StopIteration?

The iteration never ends.

It becomes an infinite iterator.

---

## Which special methods are required to create an iterator?

```
__iter__()
__next__()
```

---

# 13. Key Takeaways

✔ Iterable → Collection of elements.

✔ Iterator → Object that traverses elements one at a time.

✔ iter() converts an iterable into an iterator.

✔ next() returns the next element.

✔ StopIteration ends iteration.

✔ for loops internally use iter() and next().

✔ Custom iterators require __iter__() and __next__().

✔ Every iterator is iterable.

✔ Not every iterable is an iterator.

✔ If StopIteration is never raised, iteration becomes infinite.

---

# Revision Checklist

- [ ] Iterable
- [ ] Iterator
- [ ] iter()
- [ ] next()
- [ ] StopIteration
- [ ] Difference between Iterable & Iterator
- [ ] for loop internal working
- [ ] __iter__()
- [ ] __next__()
- [ ] Custom Iterator
- [ ] Iterator Protocol
- [ ] Interview Questions