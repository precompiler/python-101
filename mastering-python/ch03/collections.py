#list
l = list((1, 2, 3, 4, 5))
l2 = list(range(10))
l3 = [-1, -2, -3, -4]

print("List => %r List2 => %r List3 => %r" %(l, l2, l3))

filtered_list = list(filter(lambda num: num % 2 == 0, l2))

print(filtered_list)

print(l[0])

print(l[1:4])

tup_list = list((("key", "value"), ("key1", "value1")))
for k, v in tup_list:
    print(k, "->", v)

#set
colors = set(("red", "green", "blue"))
for c in colors:
    print(c)

#dict
d = dict()
d["key"] = "value"
d["key1"] = "value1"
for key in d.keys():
    print(d[key])

#tuple
t = ("a", 1, "c")
print(t[2])