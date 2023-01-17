"""
Классная точка 3.0

Давайте расширим функционал класса, написанного вами в задаче «Классная точка 2.0».

Создайте класс PatchedPoint — наследника уже написанного вами Point.

Требуется реализовать следующие виды инициализации нового класса:

параметров не передано — координаты точки равны 0;
передан один параметр — кортеж с координатами точки;
передано два параметра — координаты точки.
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.


Ввод:
point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

Вывод:
0 0
2 -3
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

