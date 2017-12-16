import contextlib

@contextlib.contextmanager
def open_context_manager(filename, mode="r"):
    fh = open(filename, mode)
    yield fh
    fh.close()

with open_context_manager("ContextWrapper.py") as fh:
    print(fh)
    print("test done")


@contextlib.contextmanager
def debug(name):
    print("Debugging {}".format(name))
    yield
    print("End")

@debug("test")
def test():
    print("Test method")

test()