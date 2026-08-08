# ⚙️ Multiprocessing in Python

> A complete guide to Python Multiprocessing, Processes, CPU-bound programming, Inter-Process Communication (IPC), Process Pools, and Best Practices with practical examples.

---

# 📖 Table of Contents

1. Introduction
2. What is a Process?
3. Why Multiprocessing?
4. Process vs Thread
5. Creating a Process
6. Starting and Joining Processes
7. Multiple Processes
8. Process Lifecycle
9. Process Memory
10. Inter-Process Communication (IPC)
11. Process Pools
12. Multiprocessing vs Threading
13. Real-World Applications
14. Best Practices
15. Common Mistakes
16. Interview Questions
17. Summary
18. Cheat Sheet

---

# 1️⃣ Introduction

A **Process** is an independent execution unit that has its own memory, resources, and Python interpreter.

Unlike threads, processes do **not** share memory by default.

```
Computer

│

├── Process 1

├── Process 2

└── Process 3
```

Each process runs independently.

---

# 2️⃣ What is a Process?

A process consists of:

- Program Code
- Memory
- Variables
- Resources
- Execution State

Example

```
Google Chrome

├── Tab 1

├── Tab 2

└── Tab 3
```

Each tab can run in a separate process.

---

# 3️⃣ Why Multiprocessing?

Suppose a task takes

```
10 seconds
```

Without multiprocessing

```
Task 1

↓

Task 2

↓

Task 3

↓

30 seconds
```

With multiprocessing

```
CPU Core 1 → Task 1

CPU Core 2 → Task 2

CPU Core 3 → Task 3
```

Total time becomes much smaller because tasks run in parallel.

---

# 4️⃣ Process vs Thread

| Process | Thread |
|----------|---------|
| Independent | Exists inside a process |
| Separate memory | Shared memory |
| Heavyweight | Lightweight |
| More secure | Faster communication |
| CPU-bound tasks | I/O-bound tasks |

---

# 5️⃣ Creating a Process

Import

```python
from multiprocessing import Process
```

Example

```python
from multiprocessing import Process

def greet():
    print("Hello Process")

p = Process(target=greet)

p.start()

p.join()

print("Program Finished")
```

Output

```
Hello Process

Program Finished
```

---

# 6️⃣ Starting and Joining Processes

## start()

Starts a new process.

```python
p.start()
```

---

## join()

Waits until the process completes.

```python
p.join()
```

Without

```python
join()
```

the main program may finish before the child process.

---

# 7️⃣ Multiple Processes

```python
from multiprocessing import Process

def task():
    print("Running")

p1 = Process(target=task)
p2 = Process(target=task)

p1.start()
p2.start()

p1.join()
p2.join()

print("Finished")
```

Output

```
Running

Running

Finished
```

Execution order may vary.

---

# 8️⃣ Process Lifecycle

```
Created

↓

Ready

↓

Running

↓

Waiting (Optional)

↓

Terminated
```

Methods

```
Process()

↓

start()

↓

join()

↓

Finished
```

---

# 9️⃣ Process Memory

Each process has its own memory.

```
Process 1

│

Variable = 10

--------------------

Process 2

│

Variable = 10
```

Changing a variable in one process does **not** affect another process.

This isolation makes multiprocessing safer than threading.

---

# 🔟 Inter-Process Communication (IPC)

Since processes have separate memory, they need special mechanisms to communicate.

Python provides:

- Queue
- Pipe
- Manager
- Shared Memory

---

## Queue

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello")

q = Queue()

p = Process(target=worker, args=(q,))

p.start()

print(q.get())

p.join()
```

Output

```
Hello
```

Queues are the most common IPC mechanism.

---

## Pipe

A Pipe creates a communication channel between two processes.

```python
from multiprocessing import Pipe
```

Useful for two-way communication.

---

# 1️⃣1️⃣ Process Pool

Instead of creating processes manually,

Python provides a Pool.

```python
from multiprocessing import Pool

def square(x):
    return x*x

with Pool() as pool:

    result = pool.map(square, [1,2,3,4])

print(result)
```

Output

```
[1,4,9,16]
```

Pool automatically manages worker processes.

---

# 1️⃣2️⃣ Multiprocessing vs Threading

| Feature | Threading | Multiprocessing |
|----------|-----------|-----------------|
| Memory | Shared | Separate |
| Best For | I/O-bound | CPU-bound |
| GIL | Affected | Not affected |
| Speed | Better for waiting tasks | Better for computation |
| Communication | Easy | Requires IPC |

---

# 1️⃣3️⃣ Real-World Applications

Multiprocessing is widely used in:

### AI Training

Different models train simultaneously.

---

### Image Processing

Thousands of images processed in parallel.

---

### Scientific Computing

Large mathematical calculations.

---

### Video Processing

Each process handles different video frames.

---

### Data Analysis

Large datasets divided among multiple processes.

---

# 1️⃣4️⃣ Best Practices

✔ Use multiprocessing for CPU-intensive tasks.

✔ Always call `join()`.

✔ Use `Pool` for many similar tasks.

✔ Use `Queue` for communication.

✔ Keep processes independent whenever possible.

---

# 1️⃣5️⃣ Common Mistakes

## ❌ Using Multiprocessing for I/O

Downloading files

Reading files

API calls

These are better handled using **Threading** or **Async Programming**.

---

## ❌ Forgetting `join()`

May cause the main program to finish early.

---

## ❌ Sharing Variables Directly

Processes have separate memory.

Use

- Queue
- Pipe
- Shared Memory

instead.

---

## ❌ Creating Too Many Processes

Too many processes increase overhead and reduce performance.

---

# 1️⃣6️⃣ Interview Questions

### Q1. What is multiprocessing?

### Q2. Difference between process and thread?

### Q3. Why is multiprocessing better for CPU-bound tasks?

### Q4. What is the GIL?

### Q5. What does `start()` do?

### Q6. Why do we use `join()`?

### Q7. What is a Process Pool?

### Q8. What is IPC?

### Q9. Difference between Queue and Pipe?

### Q10. When should you choose multiprocessing over threading?

---

# 1️⃣7️⃣ Summary

✔ Processes

✔ Process Creation

✔ start()

✔ join()

✔ Separate Memory

✔ Queue

✔ Pipe

✔ Process Pool

✔ IPC

✔ CPU-bound Tasks

✔ Best Practices

---

# 1️⃣8️⃣ Cheat Sheet

## Import

```python
from multiprocessing import Process
```

---

## Create Process

```python
p = Process(target=func)
```

---

## Start Process

```python
p.start()
```

---

## Wait for Process

```python
p.join()
```

---

## Queue

```python
from multiprocessing import Queue
```

---

## Pool

```python
from multiprocessing import Pool
```

---

## Pool Example

```python
with Pool() as pool:

    result = pool.map(func, iterable)
```

---

# 🎯 Key Takeaways

- A process is an independent execution unit with its own memory.
- Multiprocessing is ideal for **CPU-bound** tasks such as AI model training, simulations, and mathematical computations.
- Each process has its own Python interpreter, avoiding the Global Interpreter Lock (GIL).
- Use `Queue`, `Pipe`, or other IPC mechanisms to communicate between processes.
- Process Pools simplify running the same task across multiple inputs.
- Multiprocessing is a powerful tool for parallel computing and high-performance applications.

---

⭐ If you found this helpful, consider starring the repository!