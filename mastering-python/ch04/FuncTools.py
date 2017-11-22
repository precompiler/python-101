import functools


def power(m, n):
    return m ** n

print(power(3, 2))

square = functools.partial(power, n=2)

print(square(2))

print(square(10))
