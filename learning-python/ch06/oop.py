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

class Rectangle():
    width = 0
    length = 0
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length

r = Rectangle(10, 20)
print(r.area())

class VideoCard():
    brand = "Unknown"
    def start(self):
        print("Initialize video card ", self.brand)

class Gtx1080(VideoCard):
    brand = "Gtx1080"

class Gtx1050(VideoCard):
    brand = "Gtx1050"

class Laptop():
    video_card = VideoCard
    def start(self):
        self.video_card.start()

class AW17(Laptop):
    video_card = Gtx1080()

class AW15(Laptop):
    video_card = Gtx1050()

AW17().start()
AW15().start()

class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class EBook(Book):
    def __init__(self, title, publisher, pages, format):
        Book.__init__(self, title, publisher, pages)
        self.format = format

book = EBook("Demo Book", "Null", 200, "PDF")
print(book.title, book.publisher, book.pages, book.format)


class System:
    @staticmethod
    def println(str):
        print(str + "\n")

System.println("Hello world")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)
    @classmethod
    def from_point(cls, pt):
        return cls(pt.x, pt.y)

point1 = Point(1, 2)
point2 = Point.from_tuple((3, 4))
point3 = Point.from_point(point1)


class A:
    def __init__(self, factor):
        self._factor = factor

    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))

class B(A):
    def op2(self, factor):
        self._factor = factor
        print('Op2 with factor {}...'.format(self._factor))


obj = B(100)
obj.op1()    # Op1 with factor 100...
obj.op2(42)  # Op2 with factor 42...
obj.op1()    # Op1 with factor 42...
print(obj.__dict__.keys())

class A1:
    def __init__(self, factor):
        self.__factor = factor

    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))

class B1(A1):
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))


obj = B1(100)
obj.op1()    # Op1 with factor 100...
obj.op2(42)  # Op2 with factor 42...
obj.op1()    # Op1 with factor 42...
print(obj.__dict__.keys())


