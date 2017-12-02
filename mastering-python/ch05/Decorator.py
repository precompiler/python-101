import functools


def logParams(function):
    @functools.wraps(function) # use this to prevent loss of function attributes
    def wrapper(*args, **kwargs):
        print("function: {}, args: {}, kwargs: {}".format(function.__name__, args, kwargs))
        return function(*args, **kwargs)
    return wrapper


def add(a, b):
    return a + b


@logParams
def mul(a, b):
    return a * b

add(1, 1)
mul(2, 2)

def memo(function):
    function.cache = dict()
    @functools.wraps(function)
    def wrapper(*args):
        if args not in function.cache:
            function.cache[args] = function(*args)
        return function.cache[args]
    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(1, 10):
    print("fib{}:{}".format(i, fib(i)))
