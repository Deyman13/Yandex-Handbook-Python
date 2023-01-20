"""
Валидация имени

При регистрации в различных сервисах пользователи вводят большое количество информации. 
Правильное заполнение полей — важная часть работы программы, поэтому формы снабжают системами валидации данных.

Напишите функцию name_validation, которая принимает один позиционный аргумент — фамилию или имя.

Если параметр не является строкой, то вызовите исключение TypeError.

А также разработайте собственные ошибки:

CyrillicError — вызывается, если значение не состоит только из кириллических букв;
CapitalError — вызывается, если значение не начинается с заглавной буквы или найдена заглавная буква 
не в начале значения.
Обработка ошибок должна происходить в порядке, указанном в задании.

В случае успешного выполнения, функция должна вернуть переданный параметр без изменений.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
print(name_validation("user"))

Вывод:
Вызвано исключение CyrillicError
"""

class CyrillicError(Exception):
    pass 


class CapitalError(Exception):
    pass 


def name_validation(name):
    try:
        if not isinstance(name, str):
            raise TypeError
        if not all(i.casefold() in set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for i in name):
            raise CyrillicError
        if name != name.title() or any(i.isupper() for i in name if i != name[0]):
            raise CapitalError
    except TypeError:
        return "Вызвано исключение TypeError"
    except CyrillicError:
        return "Вызвано исключение CyrillicError"
    except CapitalError:
        return "Вызвано исключение CapitalError"
    return name 


    