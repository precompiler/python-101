class Demo:
    def __init__(self, info):
        self.info = info
    def __len__(self):
        return len(self.info)
    def __bool__(self):
        return "abc" in self.info

d = Demo("this is abc test")
b = Demo("Hello World")

print(len(d))
print(bool(d))

print(len(b))
print(bool(b))

