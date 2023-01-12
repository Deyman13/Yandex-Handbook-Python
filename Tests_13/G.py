"""
Классный прямоугольник 3.0

Необходимо ещё немного доработать предыдущую задачу.

Разработайте методы:

turn() — поворачивает прямоугольник на 90&deg; по часовой стрелке вокруг его центра;
scale(factor) — изменяет размер в указанное количество раз, тоже относительно центра.
Все вычисления производить с округлением до сотых.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')

Вывод:
(-3.14, 2.71)
(6.28, 5.42)
(-2.71, 3.14)
(5.42, 6.28)
"""

class Rectangle:
    def __init__(self, first_coord, sec_coord):
        self.first_coord = first_coord
        self.sec_coord = sec_coord
        self.width = abs(first_coord[0] - sec_coord[0])
        self.height = abs(first_coord[1] - sec_coord[1])
        self.center = ((first_coord[0] + sec_coord[0]) / 2, (first_coord[1] + sec_coord[1]) / 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return (round(-self.first_coord[0], 2), round(self.first_coord[1], 2))

    def get_size(self):
        return (round(self.width, 2), round(self.height, 2))

    def move(self, dx, dy):
        self.first_coord = (self.first_coord[0] + dx, self.first_coord[1] + dy)
        self.sec_coord = (self.sec_coord[0] + dx, self.sec_coord[1] + dy)
        self.center = ((self.first_coord[0] + self.sec_coord[0]) / 2, (self.first_coord[1] + self.sec_coord[1]) / 2)

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        
    def turn(self):
        dx, dy = self.sec_coord[0] - self.center[0], self.sec_coord[1] - self.center[1]
        self.first_coord = (-dy + self.center[0], -dx + -self.center[1])
        self.sec_coord = (dx + self.center[0], dy + self.center[1])
        self.width, self.height = self.height, self.width
        self.center = ((self.first_coord[0] + self.sec_coord[0]) / 2, (self.first_coord[1] + self.sec_coord[1]) / 2)

    def scale(self, factor):
        self.width *= factor
        self.height *= factor
        self.first_coord = (round(self.first_coord[0] * factor, 2), round(self.first_coord[1] * factor, 2))
        self.sec_coord = (self.first_coord[0] + self.width, self.first_coord[1] + self.height)
        self.center = ((self.first_coord[0] + self.sec_coord[0]) / 2, (self.first_coord[1] + self.sec_coord[1]) / 2)


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')


