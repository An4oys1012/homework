import random

def igra():
    popitka = 0
    number = random.randint(1, 20)
    print("Я загадал число от 1 до 20, сможете угадать?")
    while popitka < 3:
        guess = int(input("Введите число: "))
        popitka += 1
        if guess == number:
            break
    if guess == number:
        print("Правильно, вы угадали мое число, использовав", popitka, "попыток!")
    else:
        print("Ты не угадал. Я загадал число ", number)
    choice = int(input("Хотите попробовать еще раз? Если ДА, то введите 0, если НЕТ, то введите 1. Ваш выбор: "))
    if choice == 0:
        igra()
    elif choice >= 2:
        print("Вы сделали неверный выбор! До свидания!")
    elif choice == 1:
        print("До свидания!")
igra()

