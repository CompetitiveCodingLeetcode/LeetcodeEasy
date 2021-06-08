def fibonacci(n: int):
    assert 0 <= n == int(n), "Please input positive numbers only"
    if n in [0,1]:
        return n
    else:
        print(fibonacci(n-2)+fibonacci(n-1))
        return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(3)
