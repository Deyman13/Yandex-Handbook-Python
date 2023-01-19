"""
Дроби v0.7

"Остался последний штрих!" Правда звучит как издевательство?

Мы «научили» наши дроби работать с целыми числами и вот теперь надо провернуть обратное действие. 
Реализуйте функционал, который позволит производить все арифметические операции с дробями и числами, 
независимо от их положения (слева или справа) в операторе.

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
            self.x, self.y = x, 1 if y is None else y
        elif isinstance(x, str):
            if '/' in x:
                x = x.split("/")
                self.x, self.y = int(x[0]), int(x[1])
            else:
                self.x, self.y = int(x), 1
        if self.y < 0:
            self.x = -self.x
            self.y = -self.y
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
        if isinstance(other, int):
            other = Fraction(other, 1)
        x = self.x * other.y + other.x * self.y
        y = self.y * other.y
        return Fraction(x, y)
    
    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.x = self.x * other.y + other.x * self.y
        self.y = self.y * other.y
        self.__result()
        self.mixed_number = self.__to_mixed()
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        x = self.x * other.y - other.x * self.y
        y = self.y * other.y
        return Fraction(x, y)

    def __isub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.x = self.x * other.y - other.x * self.y
        self.y = self.y * other.y
        self.__result()
        self.mixed_number = self.__to_mixed()
        return self
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        x = self.x * other.x 
        y = self.y * other.y 
        return Fraction(x, y)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        x = self.x * other.y 
        y = self.y * other.x 
        return Fraction(x, y)
    
    def __imul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.x *= other.x 
        self.y *= other.y
        self.__result()
        self.mixed_number = self.__to_mixed()
        return self
    
    def __itruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        x = self.x * other.y
        y = self.y * other.x
        self.x = x
        self.y = y
        self.__result()
        self.mixed_number = self.__to_mixed()
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
            x = self.x * other.y + other.x * self.y
            y = self.y * other.y
        return Fraction(x, y)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
            x = other.x * self.y - self.x * other.y
            y = self.y * other.y
        return Fraction(x, y)

    def __rmul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
            x = self.x * other.x
            y = self.y * other.y
        return Fraction(x, y)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
            x = other.x * self.y
            y = other.y * self.x
        return Fraction(x, y)

    def reverse(self):
        return Fraction(self.y, self.x)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, int):
            return self.x == other and self.y == 1

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.x * other.y < other.x * self.y
        elif isinstance(other, int):
            return self.x < other * self.y
        
    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.x * other.y <= other.x * self.y
        elif isinstance(other, int):
            return self.x <= other * self.y
    
    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.x * other.y >= other.x * self.y
        elif isinstance(other, int):
            return self.x >= other * self.y

    def __ne__(self, other):
        if isinstance(other, Fraction):
            return self.x != other.x or self.y != other.y
        elif isinstance(other, int):
            return self.x != other or self.y != 1
    
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.x * other.y > other.x * self.y
        elif isinstance(other, int):
            return self.x > other * self.y

