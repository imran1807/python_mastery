# ⚡ Asynchronous Programming in Python (`asyncio`)

> A complete guide to Python Asynchronous Programming using `async`, `await`, and `asyncio` with practical examples, event loops, concurrency, best practices, and interview questions.

---

# 📖 Table of Contents

1. Introduction
2. Why Asynchronous Programming?
3. Synchronous vs Asynchronous
4. Coroutines
5. The Event Loop
6. async Keyword
7. await Keyword
8. Running Coroutines
9. asyncio.sleep()
10. Running Multiple Tasks
11. asyncio.gather()
12. Async vs Threading vs Multiprocessing
13. Real-World Applications
14. Best Practices
15. Common Mistakes
16. Interview Questions
17. Summary
18. Cheat Sheet

---

# 1️⃣ Introduction

Asynchronous Programming allows a program to perform **other tasks while waiting** for an operation to complete.

Instead of blocking execution, Python switches to another task whenever possible.

It is ideal for **I/O-bound operations** like:

- Network requests
- API calls
- Database queries
- Chat servers
- Web servers
- File downloads

---

# 2️⃣ Why Asynchronous Programming?

Suppose downloading one webpage takes 2 seconds.

Without async:

```
Request Page 1

↓

Wait 2 sec

↓

Request Page 2

↓

Wait 2 sec

↓

Request Page 3
```

Total ≈ 6 seconds

---

With async

```
Request Page 1

Request Page 2

Request Page 3

↓

Wait Together

↓

Receive Responses
```

Total ≈ 2 seconds

Instead of waiting for one request to finish before starting the next, all requests are initiated together.

---

# 3️⃣ Synchronous vs Asynchronous

## Synchronous

```
Task A

↓

Wait

↓

Task B

↓

Wait

↓

Task C
```

Each task waits for the previous one.

---

## Asynchronous

```
Task A

↓

Waiting...

↓

Task B

↓

Waiting...

↓

Task C
```

While one task waits, another task runs.

---

# 4️⃣ Coroutines

A **Coroutine** is a special function that can pause and resume execution.

Example

```python
async def greet():
    print("Hello")
```

Calling it

```python
greet()
```

does **not** execute the function.

Instead, it returns a coroutine object.

---

# 5️⃣ Event Loop

The Event Loop is the heart of asynchronous programming.

It manages all coroutines and switches between them whenever one is waiting.

```
Event Loop

↓

Task 1

↓

Waiting

↓

Task 2

↓

Waiting

↓

Task 3
```

This allows a single thread to handle many waiting tasks efficiently.

---

# 6️⃣ async Keyword

The `async` keyword defines a coroutine.

```python
async def greet():
    print("Hello")
```

Without `async`

```python
def greet():
```

it becomes a normal function.

---

# 7️⃣ await Keyword

The `await` keyword pauses the current coroutine until another asynchronous operation completes.

Example

```python
await asyncio.sleep(2)
```

This **does not block the entire program**.

Instead, it allows the event loop to run other coroutines.

---

# 8️⃣ Running Coroutines

Use

```python
import asyncio
```

Run a coroutine

```python
import asyncio

async def greet():
    print("Hello")

asyncio.run(greet())
```

Output

```
Hello
```

---

# 9️⃣ asyncio.sleep()

Instead of

```python
time.sleep(2)
```

use

```python
await asyncio.sleep(2)
```

Example

```python
import asyncio

async def task():

    print("Start")

    await asyncio.sleep(2)

    print("End")

asyncio.run(task())
```

Output

```
Start

(wait 2 seconds)

End
```

Unlike `time.sleep()`, `asyncio.sleep()` allows other coroutines to execute during the wait.

---

# 🔟 Running Multiple Tasks

Example

```python
import asyncio

async def task1():

    print("Task 1 Started")

    await asyncio.sleep(2)

    print("Task 1 Finished")

async def task2():

    print("Task 2 Started")

    await asyncio.sleep(1)

    print("Task 2 Finished")
```

These tasks can be executed together using `gather()`.

---

# 1️⃣1️⃣ asyncio.gather()

```python
import asyncio

async def task1():

    print("Task 1 Started")

    await asyncio.sleep(2)

    print("Task 1 Finished")

async def task2():

    print("Task 2 Started")

    await asyncio.sleep(1)

    print("Task 2 Finished")

async def main():

    await asyncio.gather(

        task1(),

        task2()

    )

asyncio.run(main())
```

Output

```
Task 1 Started

Task 2 Started

Task 2 Finished

Task 1 Finished
```

Both tasks execute concurrently.

---

# 1️⃣2️⃣ Async vs Threading vs Multiprocessing

| Feature | Async | Threading | Multiprocessing |
|----------|-----------|------------|----------------|
| Uses Threads | One | Multiple | Multiple Processes |
| Memory | Shared | Shared | Separate |
| Best For | Network I/O | File & Network I/O | CPU-intensive Tasks |
| GIL | Not affected by waiting | Limited by GIL | Not limited by GIL |
| Parallel CPU Execution | No | No | Yes |

---

# 1️⃣3️⃣ Real-World Applications

Async programming is widely used in:

### Web Servers

FastAPI

aiohttp

Sanic

---

### Chat Applications

Discord Bots

Telegram Bots

Slack Bots

---

### Web Scraping

Thousands of HTTP requests simultaneously.

---

### API Clients

Making hundreds of API calls concurrently.

---

### Cloud Applications

AWS

Azure

Google Cloud

---

# 1️⃣4️⃣ Best Practices

✔ Use async for I/O-bound operations.

✔ Always use `await` with asynchronous functions.

✔ Use `asyncio.gather()` for running multiple coroutines.

✔ Keep CPU-intensive work out of async functions.

✔ Prefer async frameworks when handling many network requests.

---

# 1️⃣5️⃣ Common Mistakes

## ❌ Forgetting `await`

Wrong

```python
task()
```

Correct

```python
await task()
```

---

## ❌ Calling a coroutine without an event loop

Wrong

```python
greet()
```

Correct

```python
asyncio.run(greet())
```

---

## ❌ Using `time.sleep()`

Wrong

```python
time.sleep(2)
```

Correct

```python
await asyncio.sleep(2)
```

---

## ❌ Using Async for CPU-bound Tasks

Heavy computations should use **Multiprocessing**.

---

# 1️⃣6️⃣ Interview Questions

### Q1. What is asynchronous programming?

### Q2. What is a coroutine?

### Q3. Difference between `async` and `await`?

### Q4. What does `asyncio.run()` do?

### Q5. Why use `asyncio.sleep()` instead of `time.sleep()`?

### Q6. What is an Event Loop?

### Q7. What is `asyncio.gather()`?

### Q8. Async vs Threading?

### Q9. Async vs Multiprocessing?

### Q10. When should you use async?

---

# 1️⃣7️⃣ Summary

✔ Coroutines

✔ async

✔ await

✔ Event Loop

✔ asyncio.run()

✔ asyncio.sleep()

✔ asyncio.gather()

✔ Concurrent Tasks

✔ Async vs Threading

✔ Async vs Multiprocessing

✔ Best Practices

---

# 1️⃣8️⃣ Cheat Sheet

## Import

```python
import asyncio
```

---

## Coroutine

```python
async def func():
    pass
```

---

## Run

```python
asyncio.run(func())
```

---

## Wait

```python
await asyncio.sleep(2)
```

---

## Multiple Tasks

```python
await asyncio.gather(task1(), task2())
```

---

# 🎯 Key Takeaways

- Asynchronous programming allows a single thread to manage many waiting tasks efficiently.
- Coroutines are created using the `async` keyword.
- Use `await` to pause the current coroutine without blocking the event loop.
- `asyncio.run()` starts the event loop and executes a coroutine.
- `asyncio.gather()` runs multiple coroutines concurrently.
- Async programming is ideal for high-performance network applications but not for CPU-intensive computations.

---

⭐ If you found this helpful, consider starring the repository!