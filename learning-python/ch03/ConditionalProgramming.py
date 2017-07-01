income = 15000

if income < 10000:
    taxCoefficient = 0.0
elif income < 30000:
    taxCoefficient = 0.2
elif income < 100000:
    taxCoefficient = 0.35
else:
    taxCoefficient = 0.45

print("Need to pay: ", income * taxCoefficient, "in taxes")

flag = False

if flag:
    print("a")
    print("b")

if flag:
    print("c")
print("d")

orderAmount = 300
discount = 25 if orderAmount > 100 else 0
print(discount)