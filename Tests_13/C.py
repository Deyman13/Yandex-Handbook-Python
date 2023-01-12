"""
Не нажимай красную кнопку!

Если написать предупреждение «Не нажимай красную кнопку!», то её сразу безумно хочется нажать.

Напишите класс RedButton, который описывает красную кнопку.

Класс должен реализовывать методы:

click() — эмулирует нажатие кнопки, выводит сообщение "Тревога!";
count() — возвращает количество раз, которое была нажата кнопка.
Примечание
Ваше решение должно содержать только классы и функции.
В решении не должно быть вызовов инициализации требуемых классов.

Ввод:
first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())

Вывод:
Тревога!
Тревога!
Тревога!
Тревога!
Тревога!
2 3
"""

class RedButton:

    def __init__(self):
        self.attention = False
        self.cnt = 0
    
    def click(self):
        print("Тревога!")
        self.cnt += 1
    
    def count(self):
        return self.cnt  


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())