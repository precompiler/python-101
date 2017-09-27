class Foo():
    pass

foo = Foo()
print(foo)
print(type(foo))

class Circle():
    PI = 3.14159
    def area(self):
        return self.PI * self.r ** 2

print(Circle.PI)

Circle.r = 0
print(Circle.r)

c1 = Circle()
print("---", c1.r)
c1.r = 10

c2 = Circle()
c2.r = 20

print(c1.r)
print(c2.r)

Circle.r = 0

print(c1.r, c2.r)

del c2.r
print(c2.r)

Circle.r = 2000
print(c2.r)
print(Circle.area(c2))

del Circle.r
print(c1.area())