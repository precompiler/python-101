lst = range(10)

ret = map(lambda *i: i, lst, "abcdefg")

for item in ret:
    print(item)

students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

print(type(students[0]["credits"].values()))

def decorate(student):
    return (sum(student['credits'].values()), student)

def undecorate(decorated_student):
    return decorated_student[1]

students = sorted(map(decorate, students), reverse=True)

for s in students:
    print(s)

students = list(map(undecorate, students))

for s in students:
    print(s)


a = [3, 6, 9]
b = [4, 7, 10]
c = [1, 8, 2]

r = map(lambda n: max(*n), zip(a, b, c))
for item in r:
    print(item)

d = [0, 1, 2, 3, 4]
ret = filter(lambda n: n > 2, d)
for item in ret:
    print(item)