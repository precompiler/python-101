a = dict(A = 1, Z = -1)
b = {"A": 1, "Z": -1}
c = dict(zip(["A", "Z"], [1, -1]))
d = dict([("A", 1), ("Z", -1)])
e = dict(b)

print(a == b == c == d == e)
# compare object id
print(a is b)

lst = list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5]))
print(lst)

z = zip(["a", "b", "c", "d"], [1, 2, 3])
z1 = zip(["a", "b"], [1, 2, 3])
print(list(z))
print(list(z1))

r = range(6)
print(list(zip("hell0", r)))

map = {}
map["name"] = "Scott"
map["active"] = True
print(len(map))
print(map["name"])
# no-existing entry, runtime error
# print(map["dummy"])
print(map)
del map["active"]
print(map)

# key existing check
print("salary" in map)
print("name" in map)

print(map.keys())
print(map.values())
print(map.items())

print("Scott" in map.values())

map = {"e": 1, "h": 0, "o": 4, "1": 3, "x": 4}

print(map.popitem())
print(map.popitem())
print(map.popitem())
print(map.popitem())
print(map)

map = {"e": 1, "h": -99, "o": 4, "1": 3, "x": 4}
print(map.pop("h"))
del map["e"]
print(map)

default = map.pop("dummy-key", 1000)
print(default)

print(map.get("abc"))


d = {}
d.setdefault("a", 1)
print(d)
d.setdefault("a", 5)
print(d)