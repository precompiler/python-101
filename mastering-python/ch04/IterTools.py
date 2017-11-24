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
