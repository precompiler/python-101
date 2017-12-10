import functools


def singleton(cls):
    pool = dict()
    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in pool:
            pool[cls] = cls(*args, **kwargs)
        return pool[cls]
    return _singleton

@singleton
class StringUtils:
    def __init__(self):
        print("Init StringUtils...")

a = StringUtils()
b = StringUtils()
