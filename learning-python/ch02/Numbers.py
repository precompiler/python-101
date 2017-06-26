a = 12
b = 3
print(a + b)
print(b - 1)
print(a // b)
print(a / b)
print(a * b)
print(2 ** 3)
print(2 ** 1024)

# flooring result
print(7 // 4)

print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
# non-zero is true
print(bool(-20))
print(bool(20))

print(not True)
print(not False)

print(1 + True)
print(7 - False)

print(3 * 0.1 - 0.3)

c = 1 + 2j
print(c.real)
print(c.imag)
d = 3 + 2j
print(c + d)
print(c * d)
print(c / d)

from fractions import Fraction
print(Fraction(10, 6))
print(Fraction(1, 3) + Fraction(2, 3))

f = Fraction(10, 6)
print(f.numerator)
print(f.denominator)

from decimal import Decimal as D
print(D(3.14))
print(D("3.14"))
print(D(3) * D(0.1) - D(0.3))
print(D("3") * D("0.1") - D("0.3"))