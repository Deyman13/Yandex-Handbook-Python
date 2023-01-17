"""
Дроби v0.1

Возможно, вы уже заметили, что дробные числа (float) недостаточно точные для некоторых задач. 
Для более точных математических расчётов иногда прибегают к созданию правильных рациональных 
дробей, описываемых числителем и знаменателем.

Начнём разработку класса Fraction, который реализует предлагаемые дроби.

Предусмотрите возможность инициализации дроби с помощью двух целых чисел или строки в формате <числитель>/<знаменатель>.
В случаях наличия общего делителя у числителя и знаменателя, дробь следует сократить.

А также реализуйте методы:

numerator() — возвращает значение числителя;
numerator(number) — изменяет значение числителя и производит сокращение дроби, если это необходимо;
denominator() – возвращает значение знаменателя;
denominator(number) — изменяет значение знаменателя и производит сокращение дроби, если необходимо;
__str__ — возвращает строковое представление дроби в формате <числитель>/<знаменатель>;
__repr__ — возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>).
Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все числа в данной задаче будут положительными.
Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием 
ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.
"""

class Fraction:

    def __init__(self, x, y=None):
        if isinstance(x, int):
            self.x, self.y = x, y
        elif isinstance(x, str):
            x = x.split("/")
            self.x, self.y = int(x[0]), int(x[1])
        self.__result()
        self.mixed_number = self.__to_mixed()
        
    def numerator(self, num=None):
        if num:
            self.x = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return self.x 
    
    def denominator(self, num=None):
        if num:
            self.y = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return self.y
    
    def __str__(self):
        return f'{self.x}/{self.y}'

    def __repr__(self) -> str:
        return f'Fraction({self.x}, {self.y})'
    
    def __gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x
    
    def __result(self):
        common_divisor = self.__gcd(self.x, self.y)
        self.x //= common_divisor
        self.y //= common_divisor
    
    def __to_mixed(self):
        if self.x >= self.y:
            quotient, remainder = divmod(self.x, self.y)
            return f'{quotient} {remainder}/{self.y}'

