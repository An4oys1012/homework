import time
def decor (func):
    def vremya ():
        start_time = time.time()
        func()
        print(f"На выполнение фунции затрачено {time.time() - start_time} секунд")
    return vremya

import math

@decor
def sinus():
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 0
    x = float(input('Введите угол x: '))
    x = round(math.radians(x), 2)
    sinus: float = math.sin(x)
    sinus = round(math.radians(x), 2)

    while abs(next_part) > eps:
        next_part = (-1) ** n * ((x ** (2 * n + 1)) / (math.factorial(2 * n + 1)))
        summa += next_part
        n += 1
        summa = round(math.radians(x), 2)
    print(f"summa = {summa}")
    print(f"sin(x) = {sinus}")
sinus()

@decor
def cosinus():
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 0
    x = float(input('Введите угол x: '))
    x = round(math.radians(x), 2)
    cosinus: float = math.cos(x)
    cosinus = round(math.radians(x), 2)

    while abs(next_part) > eps:
        next_part = (-1) ** n * ((x ** (2 * n)) / (math.factorial(2 * n)))
        summa += next_part
        n += 1
        summa = round(math.radians(x), 2)
    print(f"summa = {summa}")
    print(f"cos(x) = {cosinus}")
cosinus()

@decor
def func_xm():
    summa = 0
    next_part = 1
    eps = 0.0001
    k = 0
    x = int(input('Введите х: '))
    m = int(input('Введите m: '))
    while next_part > eps:
        next_part = (m ** k) * pow(math.log(1 + x),k) / math.factorial(k)
        summa += next_part
        k += 1
    print(f"summa = {summa}")
func_xm()

@decor
def ex():
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 0
    x = int(input('Введите х: '))
    n = int(input('Введите n: '))
    while next_part > eps:
        next_part = (x ** n) / (math.factorial(n))
        summa += next_part
        n += 1
    print(f"summa = {summa}")                               
ex()

@decor
def func_ln():          # работает только с числами <= 1
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 1
    x = float(input('Введите x: '))
    while abs(next_part) > eps:
        next_part = ((x ** n) / n) * ((-1) ** (n + 1))
        summa += next_part
        n += 1
    print(f"summa = {summa}")
func_ln()





