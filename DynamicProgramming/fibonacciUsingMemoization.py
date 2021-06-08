fibonacci_store = {}

def fibonacci(n):
    if n in fibonacci_store:
        print(fibonacci_store[n],end=" ")
        return fibonacci_store[n]
    if n in [1,2]:
        return 1
    value = fibonacci(n-1) + fibonacci(n-2)
    # print(value, end=" ")
    fibonacci_store[n] = value
    return value

print(fibonacci(4))