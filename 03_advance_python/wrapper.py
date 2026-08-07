def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)

    return wrapper
@decorator
def greet():
    """This greets the user."""
    print("Hello")
print(greet.__name__)

def star(func):

    def wrapper():
        print("* * *" )
        func()

    return wrapper


def dash(func):

    def wrapper():
        print("-----")
        func()

    return wrapper


@star
@dash
def hello():
    print("Hello")

hello()

def time_it(func):

    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result

    return wrapper
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"strarting{func.__name__}")
        result = func(*args, **kwargs)
        print(f"ending{func.__name__}")
        return result
    return wrapper
