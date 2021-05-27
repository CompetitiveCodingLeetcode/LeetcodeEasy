def powerOfTwo(base: int, power: int) -> int:
    assert 0 <= power == int(power), "Please input positive and integer powers only"
    if power == 0:
        return 1
    else:
        return base * powerOfTwo(base, power - 1)


print(powerOfTwo(3, 2))
