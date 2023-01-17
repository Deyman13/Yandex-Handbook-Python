"""
Классная точка 4.0

А теперь модернизируем уже новый класс PatchedPoint. Реализуйте магические методы _str__ и _repr__.

При преобразовании в строку точка представляется в формате (x, y).
Репрезентация же должна возвращать строку для инициализации точки двумя параметрами.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))

Вывод:
(0, 0)
PatchedPoint(2, -3)
"""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, step_x, step_y):
        self.x += step_x
        self.y += step_y
    
    def length(self, obj):
        return round(((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5, 2)

class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1 and (isinstance(args[0], (tuple, list, set))):
            super().__init__(args[0][0], args[0][1])
        else:
            super().__init__(args[0], args[1])
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'PatchedPoint({self.x}, {self.y})'


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))
