"""
Валидация имени пользователя

Продолжим реализацию системы валидации.

Напишите функцию userusername_validation, которая принимает один позиционный аргумент — имя пользователя:

Если параметр не является строкой, то вызовите исключение TypeError.

А также разработайте собственные ошибки:

BadCharacterError — вызывается, если значение состоит не только из латинских букв, цифр и символа 
нижнего подчёркивания;
StartsWithDigitError — вызывается, если значение начинается с цифры.
Обработка ошибок должна происходить в порядке, указанном в задании.

В случае успешного выполнения, функция должна вернуть переданный параметр без изменений.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
print(username_validation("$user_45$"))

Вывод:
Вызвано исключение BadCharacterError
"""

class BadCharacterError(Exception):
    pass 


class StartsWithDigitError(Exception):
    pass 


def username_validation(name):
    try:
        if not isinstance(name, str):
            raise TypeError
        if not all(i.casefold() in set("abcdefghijklmnopqrstuvwxyz1234567890_") for i in name):
            raise BadCharacterError 
        if name[0].isdigit():
            raise StartsWithDigitError
    except TypeError:
        return "Вызвано исключение TypeError"
    except BadCharacterError: 
        return "Вызвано исключение BadCharacterError"
    except StartsWithDigitError:
        return "Вызвано исключение StartsWithDigitError"
    return name 

print(username_validation("45_user"))


    