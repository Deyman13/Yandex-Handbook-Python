"""
Шашки
Шашки очень занимательная игра, которую достаточно легко моделировать.

Правила подразумевают наличие двух классов: игральная доска и шашка. Однако мы немного упростим себе задачу и вместо 
шашки будем манипулировать клетками, которые могут находиться в трех состояниях: пустая, белая шашка и чёрная шашка.

Разработайте два класса: Checkers и Cell.

Объекты класса Checkers при инициализации строят игральную доску со стандартным распределением клеток и должны обладать
методами:

move(f, t) — перемещает шашку из позиции f в позицию t;
get_cell(p) — возвращает объект «клетка» в позиции p.
Объекты класса Cell при инициализации принимают одно из трех состояний: W — белая шашка, B — чёрная шашка, * — пустая 
клетка, а также обладают методом status() возвращающим заложенное в ней состояние.

Координаты клеток описываются строками вида PQ, где:

P — столбец игральной доски, одна из заглавных латинских букв: ABCDEFGH;
Q — строка игральной доски, одна из цифр: 12345678.
Будем считать, что пользователь всегда ходит правильно и контролировать возможность хода не требуется.

Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
checkers = Checkers()
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()

Вывод:
XBXBXBXB
BXBXBXBX
XBXBXBXB
XXXXXXXX
XXXXXXXX
WXWXWXWX
XWXWXWXW
WXWXWXWX

Ввод:
checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()

Вывод:
XBXBXBXB
BXBXBXBX
XBXBXBXX
XXXXXXBX
XXXWXXXX
WXXXWXWX
XWXWXWXW
WXWXWXWX
"""

class Checkers:

    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        
        
    def move(self, f, t):
        self.f = f
        self.f = t
    def get_cell(self, p):
        self.p = p
        self.p = self.f
        return self.p
        
class Cell:

    def __init__(self, w, b, none):
        self.color = 0
        self.w = w
        self.b = b
        self.x = none

    def status(self):
        return self.color[self.p]

checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()





# self.board = [["X" if i % 2 == 0 else "B" for i in range(8)],
        #               ["X" if i % 2 == 1 else "B" for i in range(8)],
        #               ["X" if i % 2 == 0 else "B" for i in range(8)],
        #               ["X" for i in range(8)], ["X" for i in range(8)],
        #               ["X" if i % 2 == 1 else "W" for i in range(8)],
        #               ["X" if i % 2 == 0 else "W" for i in range(8)],
        #               ["X" if i % 2 == 1 else "W" for i in range(8)]] 
