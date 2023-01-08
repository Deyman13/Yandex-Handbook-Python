"""
Имя of the month

Разработайте функцию month, которая принимает номер месяца и обозначение языка ("ru", "en") и 
возвращает название заданного месяца в заданном языке с заглавной буквы.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
result = month(1, "en")

Вывод:
result = 'January'
"""

def month(num, language):
    months_ru = {"1": "Январь", "2": "Февраль", "3": "Март", "4": "Апрель", "5": "Май", 
                 "6": "Июнь", "7": "Июль", "8": "Август", "9": "Сентябрь", "10": "Октябрь", 
                 "11": "Ноябрь", "12": "Декабрь"}
    months_eng = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", 
                  "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", 
                  "11": "November", "12": "December"}
    if language == "ru":
        return months_ru[str(num)]
    elif language == "en":
        return months_eng[str(num)]

# Тестер
for i in range(1, 13):
    print(month(i, "ru"))
    print(month(i, "en"))