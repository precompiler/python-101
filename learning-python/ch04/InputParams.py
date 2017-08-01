def funcStr(y):
    print(y)
    y = "Modified"

x = "Hello World"

funcStr(x)

print(x)

def funcArray(param):
    param[0] = 0

arr = [1, 2, 3]

funcArray(arr)

print(arr)

def funcMessing(param):
    param = 100

funcMessing(arr)
print(arr)

def func(a, b, c):
    print(a, b, c)
func(c = 3, b = 2, a = 1)

def calcMin(*nums):
    print(nums) # tuple
    if nums: # collection eval to true if not empty
        minV = nums[0]
        for val in nums[1:]:
            if val < minV:
                minV = val
        print(minV)

calcMin(9, 8, 3, 2)

#unpacking
def unpacking(*args):
    print(args)

tup = (1, 3, 5, 7)
unpacking(tup)
unpacking(*tup)

def connect(**options):
    print(options)

o = {"url": "url", "user": "scott", "password": "123456"}
connect(**o)

def functriple(url, user, password):
    print(url, user, password)

functriple(**o)

