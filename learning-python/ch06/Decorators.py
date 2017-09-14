from time import sleep, time

def foo(pause_time):
    sleep(pause_time)

def timer(func, *args, **kwargs):
    print(args)
    print(*args)
    begin = time()
    func(*args, **kwargs)
    print(func.__name__, "->", time() - begin)

timer(foo, 1)
timer(foo, pause_time=0.5)

def timer1(func):
    def wrapper(*args, **kwargs):
        begin = time()
        func(*args, **kwargs)
        print(func.__name__, " costs ", time() - begin)
    return wrapper

foo = timer1(foo)
foo(1)
########################################

def logger(func):
    def wrapper(*args, **kwargs):
        print("start ", func.__name__) #function info is lost, since func now is wrapper
        func()
        print("end ", func.__name__)
    return wrapper

def logTime(func):
    def wrapper(*args, **kwargs):
        begin = time()
        func()
        print(func.__name__, " costs ", time() - begin)
    return wrapper

@logger
@logTime
def triggerEmail():
    print("Sending email...")

triggerEmail()

########################################
from functools import wraps
def smart_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("start ", func.__name__) #function info is kept now
        func()
        print("end ", func.__name__)
    return wrapper

def smart_logTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time()
        func()
        print(func.__name__, " costs ", time() - begin)
    return wrapper

@smart_logger
@smart_logTime
def smart_triggerEmail():
    print("Sending email...")

smart_triggerEmail()


