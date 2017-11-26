import itertools
nums = [1, 3, 8, 20, -90, 3]
print(list(itertools.accumulate(nums, lambda a, b: a + b)))

nums2 = [2, 7, 10, 100]
print(list(itertools.chain(nums, nums2)))

print(list(itertools.combinations([1, 2, 3, 4], 2)))

print(list(itertools.combinations_with_replacement([1, 2, 3, 4], 2)))


def powerset(iterable):
    return itertools.chain.from_iterable(
        itertools.combinations(iterable, i) for i in range(len(iterable) + 1)
    )

print(list(powerset(range(3))))

compressed = itertools.compress(range(10), [1, 1, 0, 1])
print(list(compressed))

print(list(itertools.dropwhile(lambda e: e < 5, range(10))))

print(list(itertools.takewhile(lambda x: x < 5, [3, 5, 6, 7, 8])))
