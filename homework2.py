from math import cos, sin, sqrt, pow
# 1
from math import sqrt, pow
a = float(input("Set a:"))
b = float(input("Set b:"))
y = a ** 2 / 3 + (a ** 2 + 4) / b + pow((a ** 2 + 4), 0.5) / 4 + pow(((a ** 2 + 4) ** 3), 0.5) / 4
print("Y =", y)

a = float(input("Set a:"))
b = float(input("Set b:"))
y = a ** 2 / 3 + (a ** 2 + 4) / b + sqrt(a ** 2 + 4) / 4 + sqrt((a ** 2 + 4) ** 3) / 4
print("Y =", y)

a = float(input("Set a:"))
b = float(input("Set b:"))
y = a ** 2 / 3 + (a ** 2 + 4) / b + (a ** 2 + 4) ** 0.5 / 4 + ((a ** 2 + 4) ** 3) ** 0.5 / 4
print("Y =", y)

# 2
x = float(input("Set x:"))
y = cos(x) + sin(x)
print("Y =", y)
print("tg(x) =", sin(x) / cos(x))
print("ctg(x) =", cos(x) / sin(x))

# 3
x = float(input("Set x:"))
y = x ** 5 + x ** 4 + x ** 3 + x ** 2 + x ** 2 + x + 1
print("Y =", y)

# 4
x = float(input("Set x:"))
a = float(input("Set a:"))
y = x ** 2 * 0.5 / (a + x)
print("Y =", y)

a = float(input("Set a:"))
b = float(input("Set b:"))
c = float(input("Set c:"))
y = (a + b) / (b + ((a + c) / (b + c)))
print ("Y = ", y)

x = float(input("Set x:"))
y = (cos(x ** 2) ** 2 + sin(2 * x - 1) ** 2) ** (1 / 3)
print("Y =", y)

x = float(input("Set x:"))
y = 5 * x + 3 * x ** 2 * pow((1 + sin(x ** 2)), 0.5)
print("Y =", y)

a = float(input("Set a:"))
b = 5 * a + 3 * a ** 2 * sqrt(1 + sin(a ** 2))
print("B =", b)

c = float(input("Set c:"))
d = 5 * c + 3 * c ** 2 * (1 + sin(c ** 2)) ** 0.5
print("D =", d)