import functools
import collections
import json


def power(m, n):
    return m ** n

print(power(3, 2))

square = functools.partial(power, n=2)

print(square(2))

print(square(10))


def doSum(a, b):
    return a + b

print(functools.reduce(doSum, range(1, 100)))

print(functools.reduce(lambda a, b: a + b, range(1, 100)))

def tree():
    return collections.defaultdict(tree)

departments = tree()
departments["DummyCompany"]["Finance"]["employees"] = ["Scott", "John", "Jane"]
departments["DummyCompany"]["IT"]["employees"] = ["Tony", "Tiger"]
print(json.dumps(departments, indent = 4))

def getValue(path, depts):
    return functools.reduce(lambda dts, key: dts[key], path.split("."), departments).items()

print(getValue("DummyCompany.IT", departments))