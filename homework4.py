import math

# 1.1
x = 0.6
while x <= 1.1:
    for n in range(10, 16):
        summa = 0
        for k in range(1, n + 1):
            summa += math.log((abs(x + k))) ** 2 * math.cos(k + (math.sin(x)) ** (1 / 5) / (k * x))
        res = 1 / 45 * (3 ** (x + n) ** (1 / 2)) + summa
        print(f"{x=}, {n=}, {res=}")
    x += 0.25
    
x = 0.6
step = 0.25
while x <= 1.1:
    for n in range(10, 16):
        summa = 0
        for k in range(1, n + 1):
            summa += math.log((abs(x + k))) ** 2 * math.cos(k + (math.sin(x)) ** (1 / 5) / (k * x))
        res = 1 / 45 * (3 ** (x + n) ** (1 / 2)) * summa
        print(f"{x=}, {n=}, {res=}")
    x += step

# 1.2
x = 0.6
exp = 2.718
while x <= 1.1:
    for n in range(10, 16):
        summa = 0
        for k in range(1, n + 1):
            summa += (x ** (k + 1) ** (1 / k) + exp ** (k - 2 / 3) ** (1 / k)) ** (1 / 2) / (1 + math.log(x))
        res = math.sin((math.pi * n) / (x + 3)) * summa
        print(f"{x=}, {n=}, {res=}")
    x += 0.25

# 1.3
x = 0.6
exp = 2.718
while x <= 1.1:
    for n in range(10, 16):
        summa = 0
        for k in range(1, n + 1):
            summa += (1 + (k + 1) / n) / (exp ** k) * ((x ** (k - 1)) ** (1 / 2)) + math.log(x)
        res = math.sin((x / n) ** 3 ** (1 / 2)) * summa
        print(f"{x=}, {n=}, {res=}")
    x += 0.25

# 1.4
x = 0.6
exp = 2.718
while x <= 1.1:
    for n in range(10, 16):
        summa = 0
        for k in range(1, n + 1):
            summa += math.sin((k - 1) / (k + 1) ** 2) + exp ** ((x / k) ** (1 / 2))
        res = math.pi / (x ** (1 / 3) + 3 / (x + 5)) * summa
        print(f"{x=}, {n=}, {res=}")
    x += 0.25