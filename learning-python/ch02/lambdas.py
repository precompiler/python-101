def is_multiple_of_five(n):
    return not n % 5

def get_multiple_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))

print(get_multiple_of_five(50))

def get_multiple_of_five_lambda(n):
    return list(filter(lambda k: not k % 5, range(n)))

print(get_multiple_of_five_lambda(50))

def calculator(func, a, b):
    return func(a, b)

print(calculator(lambda x, y: x + y, 1, 2))
print(calculator(lambda x, y: x * y, 1, 2))