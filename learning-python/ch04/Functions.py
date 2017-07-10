def matrix_mul(a, b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]

x = [[1, 2], [3,  4]]
y = [[5, 1], [2, 1]]

z = matrix_mul(x, y)
print(z)

print(list(zip(*y)))


t = [[a1 * b1 for a1 in [1, 2, 3]] for b1 in [4, 5, 6]]
print(t)

def test_func():
    test = 1
    print("test_func.test=", test)

test = 0
test_func()
print(test)

def outer():
    myvar = 1
    def inner():
        nonlocal myvar # bound to nearest enclosing scope
        myvar = 2
        print("inner.myvar=", myvar)
    inner()
    print("outer.myvar=", myvar)
myvar = 0
outer()
print("global.mywar=", myvar)