l = list((1, 2, 3, 4, 5))
l2 = list(range(10))
l3 = [-1, -2, -3, -4]

print("List => %r List2 => %r List3 => %r" %(l, l2, l3))

filtered_list = list(filter(lambda num: num % 2 == 0, l2))

print(filtered_list)


