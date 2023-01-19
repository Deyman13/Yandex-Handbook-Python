"""
НЕ РЕШЕНА ВЕРНО!!!

Дроби v0.2

Продолжим разработку класса Fraction, который реализует предлагаемые дроби.

Предусмотрите возможность задать отрицательные числитель и/или знаменатель. 
А также перепишите методы __str__ и __repr__ таким образом, чтобы информация об объекте 
согласовывалась с инициализацией строкой.

Далее реализуйте оператор математического отрицания — унарный минус.

Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все поля и методы, не требуемые в задаче, следует инкапсулировать 
(называть с использованием ведущих символов нижнего подчёркивания).

Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))

Вывод:
1/3 1/3 -1/3 -1/3
Fraction('1/3') Fraction('1/3') Fraction('-1/3') Fraction('-1/3')
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
        self.original = (self.x, self.y)

    def numerator(self, num=None):
        if num:
            self.x = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return abs(self.x)

    def denominator(self, num=None):
        if num:
            self.y = num
            self.__result()
            self.mixed_number = self.__to_mixed()
        return abs(self.y)

    def __str__(self):
        return f"{self.x}/{self.y}"

    def __repr__(self) -> str:
        return f"Fraction('{self.x}/{self.y}')"


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
            quotient = self.x // self.y
            remainder = self.x % self.y
            return f'{quotient} {remainder}/{self.y}'

    def __neg__(self):
        return Fraction(self.x, -self.y)

