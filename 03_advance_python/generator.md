# Advanced Python -- Chapter 2: Generators (`yield`)

*A complete guide to Python Generators, Generator Expressions,
`yield from`, and Infinite Generators*

## Topics

-   What are Generators?
-   Why Generators?
-   `yield`
-   `yield` vs `return`
-   Generator Functions
-   Generator Expressions
-   `yield from`
-   Infinite Generators
-   Generator vs Iterator
-   Memory Efficiency
-   Real-world Applications
-   Interview Questions
-   Coding Exercises
-   Revision Checklist

## What are Generators?

A generator is a special function that produces one value at a time
using `yield`. It pauses execution and resumes from the same place when
`next()` is called.

``` python
def numbers():
    yield 1
    yield 2
    yield 3
```

## Why Generators?

-   Lazy evaluation
-   Low memory usage
-   Faster startup
-   Ideal for huge datasets and streaming

## `yield` vs `return`

  return          yield
  --------------- -----------------
  Ends function   Pauses function
  One value       Multiple values
  State lost      State preserved

## Generator Function

``` python
def count():
    for i in range(1,6):
        yield i
```

## Generator Expression

``` python
(x*x for x in range(5))
```

Uses `()` and creates values on demand.

## `yield from`

Instead of:

``` python
for value in odd():
    yield value
```

Use:

``` python
yield from odd()
```

Works with generators, lists, tuples and strings.

## Infinite Generator

``` python
def infinite_even():
    num = 2
    while True:
        yield num
        num += 2
```

## Generator vs Iterator

-   Generator: created with `yield`
-   Iterator: implements `__iter__()` and `__next__()`

## Real-world Uses

-   AI/ML DataLoaders
-   File processing
-   Camera streams
-   Sensor data
-   Log processing

## Interview Questions

1.  What is a generator?
2.  Difference between `yield` and `return`
3.  What is `yield from`?
4.  Difference between generator and iterator?
5.  What are infinite generators?

## Practice

-   Generate 10,20,30,40,50
-   Squares using generator expression
-   Combine generators using `yield from`
-   Infinite even generator

## Revision Checklist

-   [ ] Generators
-   [ ] `yield`
-   [ ] Generator Expressions
-   [ ] `yield from`
-   [ ] Infinite Generators
-   [ ] Interview Questions

**Next Chapter:** Decorators
