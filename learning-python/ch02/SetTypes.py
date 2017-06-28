set1 = set()
set1.add(1)
set1.add(3)
set1.add(1)
set1.add(2)
print(set1)

set2 = set([1, 3, 5, 7, 9])
print(set2)


# union
print(set1 | set2)

# intersection
print(set1 & set2)

# difference
print(set1 - set2)

set3 = {"a", "b"}
print(set3)

# immutable set
set4 = frozenset([9, 10])


