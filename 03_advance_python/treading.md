# 🧵 Threading in Python

> A complete guide to Python Threading, Multithreading, the Global Interpreter Lock (GIL), synchronization basics, and best practices with practical examples.

---

# 📖 Table of Contents

1. Introduction
2. Process vs Thread
3. Why Threading?
4. Creating a Thread
5. Starting a Thread
6. Waiting for Threads (`join`)
7. Multiple Threads
8. Thread Lifecycle
9. Global Interpreter Lock (GIL)
10. Daemon Threads
11. Thread Synchronization
12. Thread Safety
13. Real-World Applications
14. Best Practices
15. Common Mistakes
16. Interview Questions
17. Summary
18. Cheat Sheet

---

# 1️⃣ Introduction

A **Thread** is the smallest unit of execution inside a process.

A single process can contain multiple threads that execute tasks concurrently.

```
Python Program (Process)

│

├── Thread 1

├── Thread 2

└── Thread 3
```

---

# 2️⃣ Process vs Thread

## Process

- Independent execution unit
- Own memory
- More resources
- More expensive to create

Example

```
Chrome

├── Tab 1

├── Tab 2

└── Tab 3
```

Each tab can be considered a separate process.

---

## Thread

- Exists inside a process
- Shares memory
- Lightweight
- Faster to create

Example

```
Word Processor

│

Typing

Spell Check

Auto Save
```

All happen inside one application.

---

# 3️⃣ Why Threading?

Without threading

```
Download File 1

↓

Download File 2

↓

Download File 3

Total = 15 seconds
```

With threading

```
Thread 1 → File 1

Thread 2 → File 2

Thread 3 → File 3
```

Total ≈ 5 seconds (for I/O-bound work).

Threading improves responsiveness and efficiency when tasks spend time waiting.

---

# 4️⃣ Creating a Thread

Import

```python
import threading
```

Create a function

```python
def greet():
    print("Hello")
```

Create the thread

```python
t = threading.Thread(target=greet)
```

Notice

```python
target=greet
```

✔ Correct

Not

```python
target=greet()
```

because we pass the function itself, not its return value.

---

# 5️⃣ Starting a Thread

Use

```python
t.start()
```

Example

```python
import threading

def greet():
    print("Hello")

t = threading.Thread(target=greet)

t.start()
```

Output

```
Hello
```

`start()` creates a new thread and begins execution.

---

# 6️⃣ Waiting for Threads (`join()`)

Sometimes the main program finishes before the thread.

Use

```python
t.join()
```

Example

```python
import threading

def greet():
    print("Hello")

t = threading.Thread(target=greet)

t.start()

t.join()

print("Done")
```

Output

```
Hello

Done
```

`join()` blocks the main thread until the worker thread completes.

---

# 7️⃣ Multiple Threads

```python
import threading

def task():
    print("Running")

t1 = threading.Thread(target=task)

t2 = threading.Thread(target=task)

t1.start()

t2.start()

t1.join()

t2.join()

print("Finished")
```

Output

```
Running

Running

Finished
```

The order of execution is not guaranteed.

---

# 8️⃣ Thread Lifecycle

```
Created

↓

Ready

↓

Running

↓

Waiting (Optional)

↓

Completed
```

Methods used

```
Thread()

↓

start()

↓

join()

↓

Completed
```

---

# 9️⃣ Global Interpreter Lock (GIL)

Python's **Global Interpreter Lock (GIL)** allows only **one thread to execute Python bytecode at a time** in CPython.

This means:

✔ Threading is excellent for **I/O-bound** tasks.

❌ Threading is not ideal for **CPU-bound** tasks.

For CPU-intensive work, use **Multiprocessing**.

---

# 🔟 Daemon Threads

A daemon thread runs in the background.

Example

```python
import threading
import time

def background():
    while True:
        print("Running...")
        time.sleep(1)

t = threading.Thread(target=background)

t.daemon = True

t.start()

print("Main Program Ends")
```

When the main program exits,

the daemon thread also stops.

Common uses

- Background monitoring
- Logging
- Auto-saving
- Periodic cleanup

---

# 1️⃣1️⃣ Thread Synchronization

Multiple threads may access the same resource.

Example

```
Thread 1

↓

Bank Balance

↑

Thread 2
```

If both modify the balance simultaneously,

unexpected results may occur.

Python provides synchronization tools such as:

- Lock
- RLock
- Semaphore
- Event
- Condition

The most common is **Lock**.

Example

```python
lock.acquire()

# Critical Section

lock.release()
```

Better

```python
with lock:
    # Critical Section
```

---

# 1️⃣2️⃣ Thread Safety

A program is **thread-safe** if multiple threads can execute correctly without corrupting shared data.

Example

```python
counter += 1
```

Two threads updating the same variable simultaneously may produce incorrect results.

Use synchronization primitives (such as `Lock`) to protect shared resources.

---

# 1️⃣3️⃣ Real-World Applications

Threading is commonly used in:

- File Downloads
- Web Scraping
- REST API Requests
- Chat Applications
- GUI Programs
- Reading Files
- Database Queries

Example

```
Download Images

↓

Thread 1

Thread 2

Thread 3
```

---

# 1️⃣4️⃣ Best Practices

✔ Use threading for I/O-bound tasks.

✔ Always call `join()` when the main program depends on thread completion.

✔ Keep thread functions small.

✔ Protect shared data using locks.

✔ Avoid creating too many threads.

---

# 1️⃣5️⃣ Common Mistakes

## ❌ Passing the result instead of the function

Wrong

```python
Thread(target=greet())
```

Correct

```python
Thread(target=greet)
```

---

## ❌ Forgetting `join()`

Without `join()`, the main program may finish before worker threads.

---

## ❌ Using Threading for CPU-bound Tasks

Heavy computations should use **Multiprocessing**.

---

## ❌ Ignoring Shared Data

Multiple threads modifying the same variable without synchronization may cause race conditions.

---

# 1️⃣6️⃣ Interview Questions

### Q1. What is a thread?

### Q2. Difference between a process and a thread?

### Q3. Why do we use `start()`?

### Q4. Why do we use `join()`?

### Q5. Why do we write `target=greet` instead of `target=greet()`?

### Q6. What is the Global Interpreter Lock (GIL)?

### Q7. Why is threading suitable for I/O-bound tasks?

### Q8. What is a daemon thread?

### Q9. What is thread synchronization?

### Q10. What is thread safety?

---

# 1️⃣7️⃣ Summary

✔ Threads

✔ Process vs Thread

✔ Thread Creation

✔ start()

✔ join()

✔ Multiple Threads

✔ Thread Lifecycle

✔ GIL

✔ Daemon Threads

✔ Thread Synchronization

✔ Thread Safety

✔ Best Practices

---

# 1️⃣8️⃣ Cheat Sheet

## Import

```python
import threading
```

---

## Create Thread

```python
t = threading.Thread(target=func)
```

---

## Start Thread

```python
t.start()
```

---

## Wait for Thread

```python
t.join()
```

---

## Daemon Thread

```python
t.daemon = True
```

---

## Lock

```python
lock.acquire()

# Critical Section

lock.release()
```

or

```python
with lock:
    # Critical Section
```

---

# 🎯 Key Takeaways

- A thread is the smallest unit of execution inside a process.
- Threads share memory, making them lightweight but requiring synchronization.
- Use `start()` to begin execution and `join()` to wait for completion.
- Threading is best suited for **I/O-bound** tasks such as file operations, API requests, and web scraping.
- The GIL prevents true parallel execution of Python bytecode in CPython, making threading less effective for CPU-intensive tasks.
- Protect shared resources using synchronization mechanisms like `Lock`.

---

⭐ If you found this helpful, consider starring the repository!