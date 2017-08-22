items = "ABCDE"
pairs = []

for a in range(len(items)):
    for b in range(len(items)):
        pairs.append((items[a], items[b]))

print(pairs)

ret = [(items[a], items[b]) for a in range(len(items)) for b in range( len(items))]

print(ret)

ret2 = [(x, y) for x in range(2) for y in range(2)]
ret3 = [(x, y) for x in range(2) for y in range(x, 2)]
print(ret2)
print(ret3)

