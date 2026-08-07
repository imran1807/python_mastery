def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper
def greet():
    print("Hello")

new_function = decorator(greet)

new_function()
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@decorator
def greet():
    print("Hello")

greet()
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper