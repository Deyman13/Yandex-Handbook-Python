"""
Классный прямоугольник 2.0

Расширим функционал класса написанного вами в предыдущей задаче.

Реализуйте методы:

get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
get_size() — возвращает размеры в виде кортежа;
move(dx, dy) — изменяет положение на заданные значения;
resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())

Вывод:
(3.2, 3.14) (4.32, 7.44)
(4.52, -1.86) (4.32, 7.44)
"""

class Rectangle:
    def __init__(self, first_coord, sec_coord):
        self.x = min(first_coord[0], sec_coord[0])
        self.y = max(first_coord[1], sec_coord[1])
        self.width = abs(first_coord[0] - sec_coord[0])
        self.height = abs(first_coord[1] - sec_coord[1])

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return (round(self.x, 2), round(self.y, 2))

    def get_size(self):
        return (round(self.width, 2), round(self.height, 2))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

