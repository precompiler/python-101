def numbers():
    yield 1
    yield 2
    yield 3

for i in numbers():
    print(i)

it = numbers()
print(next(it))
print(next(it))
print(next(it))
# next(it)


def ls():
    yield "where"
    yield "what"
    yield "www"
    yield "dummy"
    yield "when"


def grep(seq, target_str):
    for item in seq:
        if target_str in item:
            yield item

print("=" * 10)
for r in grep(ls(), "wh"):
    print(r)
