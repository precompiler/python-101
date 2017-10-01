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
