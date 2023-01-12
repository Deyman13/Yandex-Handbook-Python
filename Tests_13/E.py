"""
Классный прямоугольник

Давайте перейдём к более сложным геометрическим фигурам.

Разработайте класс Rectangle.

При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника.

Класс должен реализовывать методы:

perimeter — возвращает периметр прямоугольника;
area — возвращает площадь прямоугольника.
Все результаты вычислений нужно округлить до сотых.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

Вывод:
23.52
"""

class Rectangle:

    def __init__(self, first_coord, sec_coord):
        self.first_coord = first_coord
        self.sec_coord = sec_coord
    
    def perimeter(self):
        d1 = abs(self.sec_coord[0] - self.first_coord[0])
        d2 = abs(self.sec_coord[1] - self.first_coord[1])
        return round(2 * (d1 + d2), 2)

    def area(self):
        d1 = abs(self.sec_coord[0] - self.first_coord[0])
        d2 = abs(self.sec_coord[1] - self.first_coord[1])
        return round(d1 * d2, 2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())