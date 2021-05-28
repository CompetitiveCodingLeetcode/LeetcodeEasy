def f(i, values=[]):
    values.append(i)
    print(values)
    return values


f(1)
f(2)
f(3)
#output=[1]\n[1,2]\n[1,2,3]
