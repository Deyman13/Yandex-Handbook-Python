"""
Модернизация системы вывода

Разработайте функцию modern_print, которая принимает строку и выводит её, если она не была выведена ранее.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")

Вывод:
Hello!
How do you do?
"""

def modern_print(string):
    if string not in new_set:
        print(string)
        new_set.add(string)

        
new_set = set()
