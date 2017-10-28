import builtins
import collections
import argparse

print(vars())
print("-" * 320)
print(vars(builtins))
m = globals(), locals()
print(type(m))


def a(key):
    builtin_vars = vars(builtins)
    if key in locals():
        value = locals()[key]
    elif key in globals():
        value = globals()[key]
    elif key in builtin_vars:
        value = builtin_vars[key]
    else:
        raise NameError("name %r is not defined" %key)

a("__name__")

def b(key):
    mappings = globals(), locals(), vars(builtins)
    for mapping in mappings:
        if key in mapping:
            value = mapping[key]
            break
    else:
        raise NameError("name %r is not defined" %key)
b("__doc__")
#b("dummy")

def c(key):
    mappings = collections.ChainMap(globals(), locals(), vars(builtins))
    value = mappings[key]

c("__package__")
#c("###")

args = vars()
x = {k: v for k, v in args.items() if v}
y = {"a": "b"}
print(type(y))
print(type(x))
def d():
    defaults = {"flag": "default flag value", "list": "default list value"}
    parser = argparse.ArgumentParser()
    parser.add_argument("--flag")
    parser.add_argument("--list")
    args = vars(parser.parse_args())
    filtered_args = {k: v for k, v in args.items() if v}
    combined = collections.ChainMap(filtered_args, defaults)
    print(combined["flag"])
    #print(combined["dummy"])
d()

d1 = {"k":"v1"}
d2 = {"k":"v2"}
dc1 = collections.ChainMap(d1, d2)
dc2 = collections.ChainMap(d2, d1)
#first win
print(dc1["k"])
print(dc2["k"])

print(dc1.maps[0]["k"])
print(dc1.maps[1]["k"])
