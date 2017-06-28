x = []  # empty list
y = list()

print(type(x))
print(type(y))

z = [1, 2, 3]
print(z)

for x in [2, 3, 4]:
    print(x)

a = [x + 5 for x in [2, 3, 4]]
print(a)

c = list((1, 2, 3))
print(c)

d = list('hello')
print(d)

a = [19, 1, 2, 3, 4, 1]
a.append(5)

print(a)
print(a.count(1))
print(a.index(4))
a.sort()
print(a)
print(min(a))
print(max(a))
print(sum(a))
print(len(a))

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)