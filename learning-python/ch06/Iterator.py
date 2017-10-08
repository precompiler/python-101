class Demo:
    def __init__(self, data):
        self.data = data
        self.indices = list(range(0, len(data)))
    def __iter__(self):
        return self
    def __next__(self):
        if self.indices:
            return self.data[self.indices.pop(0)]
        raise StopIteration

d = Demo("Hello")
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))