import functools

@functools.singledispatch
def printer(value):
    print("printer -> {}".format(value))

@printer.register(str)
def str_printer(value):
    print("str_printer -> {}".format(value))

@printer.register(int)
def int_printer(value):
    print("int_printer -> {}".format(value))

@printer.register(dict)
def dict_printer(value):
    print("dict_printer -> {}".format(value))


printer("abc")
printer(100)
printer({"a": "b"})
printer([1, 2, 3, 4])
