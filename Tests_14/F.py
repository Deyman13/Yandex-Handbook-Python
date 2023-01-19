"""
Дроби v0.3

Продолжим разработку класса Fraction, который реализует предлагаемые дроби.

Реализуйте бинарные операторы:

+ — сложение дробей, создаёт новую дробь;
- — вычитание дробей, создаёт новую дробь;
+= — сложение дробей, изменяет дробь, переданную слева;
-= — вычитание дробей, изменяет дробь, переданную слева.
Примечание
Будем считать, что пользователь знает о запрете деления на ноль.
Все поля и методы, не требуемые в задаче, следует инкапсулировать 
(называть с использованием ведущих символов нижнего подчёркивания).

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
    
    def __add__(self, other):
        x = self.x * other.y + other.x * self.y
        y = self.y * other.y
        return Fraction(x, y)
    
    def __iadd__(self, other):
        self.x = self.x * other.y + other.x * self.y
        self.y = self.y * other.y
        self.__result()
        self.mixed_number = self.__to_mixed()
        return self

    def __sub__(self, other):
        x = self.x * other.y - other.x * self.y
        y = self.y * other.y
        return Fraction(x, y)

    def __isub__(self, other):
        self.x = self.x * other.y - other.x * self.y
        self.y = self.y * other.y
        self.__result()
        self.mixed_number = self.__to_mixed()
        return self


