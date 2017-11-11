#list
l = list((1, 2, 3, 4, 5))
l2 = list(range(10))
l3 = [-1, -2, -3, -4]

print("List => %r List2 => %r List3 => %r" %(l, l2, l3))

filtered_list = list(filter(lambda num: num % 2 == 0, l2))

print(filtered_list)

print(l[0])

print(l[1:4])

tup_list = list((("key", "value"), ("key1", "value1")))
for k, v in tup_list:
    print(k, "->", v)

#set
colors = set(("red", "green", "blue"))
for c in colors:
    print(c)

#dict
d = dict()
d["key"] = "value"
d["key1"] = "value1"
for key in d.keys():
    print(d[key])

#tuple
t = ("a", 1, "c")
print(t[2])

#counter
import collections
str = "Hello World"
counter = collections.Counter(str)
print("--------------")
print("|char |count |")
print("--------------")
for c in str:
    print("|%s   |%d    |" %(c, counter[c]))
print("--------------")

import math
cache = collections.Counter()
for i in range(0, 1000000):
    cache[math.sqrt(i) // 25] += 1

for key, count in cache.most_common(5):
    print("%s : %d" %(key, count))


set1 = collections.Counter("013579")
set2 = collections.Counter("02468")
print(set1 & set2)
print(set1 - set2)
print(set1 | set2)

#deque not thread safe
q = collections.deque()
q.append(1)
q.append((1, 2, 3))
print(q)
print(q.popleft())
print(q.popleft())
#q.popleft() IndexError: pop from an empty deque
import queue
safe_q = queue.Queue() # synchronized
safe_q.put("a")
print(safe_q.get_nowait())

#defaultdict
edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'a'),
    ('b', 'd'),
    ('c', 'a'),
    ('d', 'a'),
    ('d', 'b'),
    ('d', 'c')
]

graph = collections.defaultdict(list)
for start_node, end_node in edges:
    graph[start_node].append(end_node)
print(graph)

graph2 = collections.defaultdict(list)
print(graph2["x"])

import json
def tree():
    return collections.defaultdict(tree)

my_tree = tree()
my_tree["root"]["n1"] = "1"
my_tree["root"]["n2"] = "2"
my_tree["root"]["n3"] = tree()
my_tree["root"]["n3"]["n31"] = "3"
my_tree["root"]["n3"]["n32"] = "4"


print(json.dumps(my_tree, sort_keys=True, indent=4))

#named tuple
Point = collections.namedtuple("Point", ["x", "y", "z"])
print(Point)
p1 = Point(1, 2, 3)
p2 = Point(x = 4, y = 5, z = 6)
print(p1)
print(p2)

x, y, z = p1
print("{}, {}, {}".format(x, y, z))

#enumeration
import enum
class Color(enum.Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"

def display(color):
    print( {
        Color.RED : Color.RED.value,
        Color.GREEN : Color.GREEN.value,
        Color.BLUE : Color.BLUE.value
    }[color])

display(Color.RED)
display(Color.GREEN)
# display("BLUE") no match