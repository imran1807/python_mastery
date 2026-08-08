# 📊 Logging in Python

> A complete guide to Python's built-in **logging** module for debugging, monitoring, and maintaining applications with practical examples, best practices, and interview questions.

---

# 📖 Table of Contents

1. Introduction
2. Why Logging Instead of print()?
3. Logging Levels
4. Basic Logging
5. Logging to a File
6. Formatting Log Messages
7. Logging Exceptions
8. Real-World Applications
9. Best Practices
10. Common Mistakes
11. Interview Questions
12. Summary

---

# 1️⃣ Introduction

The **logging** module is Python's built-in framework for recording events that happen while a program is running.

Logging helps developers:

- Debug applications
- Monitor program execution
- Track errors
- Record important events
- Diagnose production issues

Import the module

```python
import logging
```

---

# 2️⃣ Why Logging Instead of `print()`?

Many beginners use:

```python
print("Program Started")
```

Although useful during development, `print()` has several limitations.

### Problems with `print()`

- Cannot categorize messages.
- No timestamps.
- Cannot easily save messages to a file.
- Difficult to disable or filter messages.
- Not suitable for production applications.

---

### Advantages of Logging

✔ Different logging levels

✔ Save logs to files

✔ Include timestamps

✔ Filter messages

✔ Better debugging

✔ Production-ready

---

# 3️⃣ Logging Levels

Python provides five standard logging levels.

| Level | Purpose |
|--------|----------|
| DEBUG | Detailed debugging information |
| INFO | General application events |
| WARNING | Something unexpected happened, but the program continues |
| ERROR | An operation failed |
| CRITICAL | Serious error that may stop the application |

Priority

```
DEBUG

↓

INFO

↓

WARNING

↓

ERROR

↓

CRITICAL
```

---

# 4️⃣ Basic Logging

Configure logging

```python
import logging

logging.basicConfig(level=logging.INFO)
```

Example

```python
logging.info("Application Started")
```

Output

```
INFO:root:Application Started
```

---

### Example with Multiple Levels

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug Message")

logging.info("Information")

logging.warning("Warning")

logging.error("Error")

logging.critical("Critical Error")
```

Output

```
DEBUG:root:Debug Message

INFO:root:Information

WARNING:root:Warning

ERROR:root:Error

CRITICAL:root:Critical Error
```

---

# 5️⃣ Logging to a File

Instead of displaying logs on the terminal,

save them into a file.

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application Started")
```

Python creates

```
app.log
```

Contents

```
INFO:root:Application Started
```

---

# 6️⃣ Formatting Log Messages

Logging becomes much more useful with timestamps.

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Server Started")
```

Output

```
2026-08-08 10:30:21 - INFO - Server Started
```

---

### Common Format Specifiers

| Specifier | Description |
|------------|-------------|
| %(asctime)s | Timestamp |
| %(levelname)s | Log level |
| %(message)s | Log message |
| %(filename)s | File name |
| %(funcName)s | Function name |
| %(lineno)d | Line number |

Example

```python
format="%(levelname)s : %(message)s"
```

Output

```
WARNING : Low Battery
```

---

# 7️⃣ Logging Exceptions

Instead of only printing an error,

log it.

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0

except Exception as e:
    logging.error(e)
```

Output

```
ERROR:root:division by zero
```

---

# 8️⃣ Real-World Applications

Logging is used in almost every production application.

### Web Applications

```
User Login

User Logout

Payment Successful

Payment Failed
```

---

### Machine Learning

```
Dataset Loaded

Training Started

Epoch Completed

Validation Accuracy

Training Finished
```

---

### Backend Services

```
Server Started

Client Connected

API Request Received

Database Connected
```

---

### Automation Scripts

```
File Downloaded

Email Sent

Backup Completed
```

---

# 9️⃣ Best Practices

✔ Use logging instead of `print()`.

✔ Choose the correct logging level.

✔ Log meaningful messages.

✔ Include timestamps.

✔ Save logs to files in production.

✔ Avoid logging sensitive information such as passwords or API keys.

✔ Use consistent formatting.

---

# 🔟 Common Mistakes

## ❌ Using `print()` everywhere

Instead

```python
logging.info(...)
```

---

## ❌ Logging everything as ERROR

Incorrect

```python
logging.error("Application Started")
```

Correct

```python
logging.info("Application Started")
```

---

## ❌ Ignoring log levels

Choose levels appropriately.

Example

```
DEBUG

↓

INFO

↓

WARNING

↓

ERROR

↓

CRITICAL
```

---

## ❌ Logging confidential information

Avoid logging

- Passwords
- Credit Card Numbers
- API Keys
- Tokens

---

# 1️⃣1️⃣ Interview Questions

### Q1. Why is logging preferred over `print()`?

### Q2. Name the five logging levels.

### Q3. Difference between INFO and DEBUG?

### Q4. Difference between ERROR and CRITICAL?

### Q5. What does

```python
logging.basicConfig()
```

do?

### Q6. How do you save logs to a file?

### Q7. Why are timestamps useful?

### Q8. What is the purpose of the `format` parameter?

---

# 📚 Summary

✔ Logging Module

✔ Logging Levels

✔ basicConfig()

✔ File Logging

✔ Log Formatting

✔ Exception Logging

✔ Production Logging

✔ Best Practices

✔ Common Mistakes

---

# 🎯 Key Takeaways

- Logging is the standard way to record application events.
- It is more powerful and flexible than `print()`.
- Use appropriate log levels to categorize messages.
- Save logs to files for production applications.
- Include timestamps and useful formatting.
- Never log sensitive information.
- Logging is essential for debugging, monitoring, and maintaining professional Python applications.

---

# 📌 Cheat Sheet

## Import

```python
import logging
```

---

## Basic Configuration

```python
logging.basicConfig(level=logging.INFO)
```

---

## Log Messages

```python
logging.debug("Debug")

logging.info("Info")

logging.warning("Warning")

logging.error("Error")

logging.critical("Critical")
```

---

## Save to File

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
```

---

## Custom Format

```python
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

---

⭐ If you found this helpful, consider starring the repository!