t = ()
print(type(t))

# treat as int
t1 = (1)
print(t1)
print(type(t1))

t2 = (1, )
print(t2)
print(type(t2))

t3 = (1, 2, 3)
print(t3)
print(type(t3))

t4 = 1, 2, 3
t5 = (1, 2, 3)
print(t4 == t5)

a = 1
b = 2
a, b = b, a
print(a)
print(b)
