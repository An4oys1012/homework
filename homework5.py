# Проверка числа на простоту с использованием рекурсии

n = int(input("Введите число: "))


def prost(n, i=None):
    if i is None:
        i = n - 1
    while i != 1:
        if n % i == 0:
            print("Число", n, "не является простым")
            return False
        else:
            return prost(n, i - 1)
    else:
        print("Число", n, "является простым")
        return True


prost(n)

# Нахождение наибольшего общего делителя (НОД) при помощи рекурсии

a = int(input("Введите число: "))
b = int(input("Введите число: "))


def NOD(a, b):
    if b == 0:
        print("Наибольший общий делитель равен", a)
    else:
        return NOD(b, a % b)


NOD(a, b)

# Бинарный поиск
from random import randint

lst = []
for i in range(10):  # Создание списка,
    lst.append(randint(1, 50))
lst.sort()  # его сортировка по возрастанию
print(lst)

n = int(input('Введите число для поиска: '))

low = 0
high = len(lst) - 1
mid = len(lst) // 2

while lst[mid] != n and low <= high:
    if n > lst[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Заданного числа нет в списке")
else:
    print("Индекс заданного числа =", mid)
