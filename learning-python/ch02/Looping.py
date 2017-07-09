for i in [1, 2, 3, 4]:
    print(i)

for i in range(5):
    print(i)

colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(i, colors[i])

for color in colors:
    print(color)

for idx, color in enumerate(colors):
    print(idx, color)

people = ["Scott", "John", "Mike"]
ages = [50, 30, 25]
for person, age in zip(people, ages):
    print(person, age)

for data in zip(people, ages):
    print(data)

arr = [1, 2, 3, 4, 5, 6]
print(arr)
arr = arr[::-1]
print(arr)

empid = 2
class NoResourceFoundException(Exception):
    pass
emps = {1: "Scott", 2: "John", 3: "Tiger"}
for emp in emps.items():
    if emp.__contains__(empid):
        print("Found")
        break
else:
    raise NoResourceFoundException("Not found")

from itertools import count
for n in count(5, 3):
    if n > 20:
        break
    print(n, end=", ")
print()
from itertools import compress
ret = compress("abcdefg", (1, 0, 1, 1))
for x in ret:
    print(x)

data = range(10)
even = [1, 0] * 10
odd = [0, 1] * 10
evenNumbers = compress(data, even)
oddNumbers = compress(data, odd)
print(list(data))
print(list(evenNumbers))
print(list(oddNumbers))

from itertools import permutations, combinations
print(list(permutations("ABC")))
print(list(combinations("ABC", 2)))

