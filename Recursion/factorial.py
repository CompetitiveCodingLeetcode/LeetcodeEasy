def factorial(n: int) -> int:
    assert 0 <= n == int(n), "Please input positive numbers only"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


factorial(1.8)
