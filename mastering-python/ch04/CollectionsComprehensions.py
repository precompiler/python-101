#List

l = [x for x in range(1, 10)]
print(l)

l2 = [x ** 2 for x in range(1, 10)]
print(l2)

l3 = [x for x in range(1, 10) if x % 2 == 0]
print(l3)

tlist = [(x, y) for x in range(1, 3) for y in (5, 7)]
print(tlist)

print(list(range(10)))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for x in matrix:
    print(x)
print("-----------")
print ([y for x in matrix for y in x])