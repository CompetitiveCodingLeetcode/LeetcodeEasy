from functools import lru_cache

# fibonacci_store = {}
@lru_cache(1000)
def fibonacci(n):
    # if n in fibonacci_store:
    #     print(fibonacci_store[n],end=" ")
    #     return fibonacci_store[n]
    if n in [1,2]:
        return 1
    value = fibonacci(n-1) + fibonacci(n-2)
    # print(value, end=" ")
    # fibonacci_store[n] = value
    return value

n=4
for i in range(1,n+1):
    print(fibonacci(i))