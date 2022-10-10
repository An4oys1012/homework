# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов

res = ["Иванов Олег 4", "Петров Иван 3", "Дмитриев Игорь 2", "Юрьева Кира 5", "Сидорова Мария 1"]

with open('marks.txt', "w", encoding='utf-8') as f:
    for text in res:
        f.writelines(text)
        if res.index(text) != len(res) - 1:
            f.writelines("\n")

with open('marks.txt', encoding='utf-8') as f:
    data = f.read()
    for line in data:
        #length_line = len(line)
        for i in range(len(line)):
            if line[i].isdigit():
                mark = int(line[i])
                if mark < 3:
                    print("Студент, чья оценка по группе меньше 3 баллов:", line)




