"""
Классная точка 5.0

Согласитесь, что использовать операторы куда удобнее, чем обыкновенные методы. 
Давайте вспомним о реализованном нами методе move(x, y) и напишем ему альтернативу в виде операторов + и +=.

При выполнении кода point + (x, y), создаётся новая точка, которая отличается от изначальной на 
заданное кортежем расстояние по осям x и y.

При выполнении кода point += (x, y) производится перемещение изначальной точки.

Напомним, что сейчас мы модернизируем только класс PatchedPoint.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)

Вывод:
(0, 0)
(0, 0) (2, -3) False
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
    
    def __add__(self, other):
        new_point = PatchedPoint(self.x + other[0], self.y + other[1])
        return new_point
    
    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)

