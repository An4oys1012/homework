"""Разработать класс SuperStr, который наследует функциональность стандартного типа str и
содержит 2 новых метода:
 • метод is_repeatance (s), который принимает 1 аргумент s и возвращает True или False
 в зависимости от того, может ли текущая строка быть получена целым количеством повторов строки s.
 Вернуть False, если s не является строкой. Считать, что пустая строка не содержит повторов.
 • метод is_palindrom (), который возвращает True или False в зависимости от того, является ли строка палиндромом.
 Регистрами символов пренебрегать. Пустую строку считать палиндромом."""

class SuperStr(str):
    def __init__(self, string):
        self.string = string

    def is_repeatance(self, s):
        string = self.string
        if not isinstance(s, str):
            return False
        n = len(string) // (len(s) or 1)
        return string == n * s

    def is_palindrom(self, st):
        if st == "":
            return True
        st = st.lower()
        return st == st[::-1]

a = SuperStr("123123123123")

print(a.is_repeatance(""))
print(a.is_repeatance(123))
print(a.is_repeatance("123123123123"))
print(a.is_repeatance("123123"))
print(a.is_repeatance("123"))
print(a.is_repeatance("123123123123123"))

print(a.is_palindrom(""))
print(a.is_palindrom("anna"))
print(a.is_palindrom("123_321"))
print(a.is_palindrom("123321"))
print(a.is_palindrom("asdfghjk"))





