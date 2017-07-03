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
