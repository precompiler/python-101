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
