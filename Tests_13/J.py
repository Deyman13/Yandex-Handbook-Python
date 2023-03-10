"""
Стек

Ещё одной полезной коллекцией является стек реализующий принцип «Последний пришёл – первый ушёл». 
Его часто представляют как стопку карт или магазин пистолета, где приходящие элементы закрывают 
выход уже находящимся в коллекции.

Реализуйте класс Stack, который не имеет параметров инициализации, но поддерживает методы:

push(item) — добавить элемент в конец стека;
pop() — «вытащить» первый элемент из стека;
is_empty() — проверяет стек на пустоту.
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")

Вывод:
9 8 7 6 5 4 3 2 1 0 
"""

# По сути единственное различие от прошлой задачи в pop(0), а тут pop() без передачи доп аргумента... 

class Stack:

    def __init__(self):
        self.st = []
    
    def push(self, item):
        self.st.append(item)
    
    def pop(self):
        return self.st.pop()
    
    def is_empty(self):
        return not bool(self.st)
