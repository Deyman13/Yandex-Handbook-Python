"""
Работа не волк

Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов. 
Каждая должность имеет собственный оклад (заработную плату за час работы). В нашей импровизированной компании 
существуют 3 должности:

Junior — с окладом 10 тугриков в час;
Middle — с окладом 15 тугриков в час;
Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю). 
Класс реализует следующие методы:

work(time) — отмечает новую отработку в количестве часов time;
rise() — повышает программиста;
info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

Вывод:
Васильев Иван 750ч. 7500тгр.
Васильев Иван 1250ч. 15000тгр.
Васильев Иван 1500ч. 20000тгр.
Васильев Иван 1750ч. 25250тгр.
"""


class Programmer:

    def __init__(self, name, pos, time=0):
        self.name = name
        self.pos = pos
        self.time = time
        self.salary = 10 if pos == "Junior" else 15 if pos == "Middle" else 20
        self.temp = 0

    def work(self, time):
        self.time += time
        self.temp += self.salary * time

    def rise(self):
        if self.pos == "Junior":
            self.pos = "Middle"
            self.salary += 5
        elif self.pos == "Middle":
            self.pos = "Senior"
            self.salary += 5
        elif self.pos == "Senior":
            self.salary += 1
        return self.salary

    def info(self):
        return f'{self.name} {self.time}ч. {self.temp}тгр.'


programmer = Programmer('Васильев Иван', 'Middle')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
