def sumOfDigits(num: int) -> int:
    assert 0 <= num == int(num), "Please input positive numbers only"
    if num == 0:
        return 0
    return int(num % 10) + sumOfDigits(int(num / 10))


print(sumOfDigits(590))
