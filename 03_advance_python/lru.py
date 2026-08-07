from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)

print(factorial(5))
print(factorial.cache_info())