"""
Валидация пользователя

Используйте две предыдущих функции валидации и напишите функцию user_validation, которая принимает 
именованные аргументы:

last_name — фамилия;
first_name — имя;
username — имя пользователя.

Если функции был передан неизвестный параметр или не передан один из обязательных, то вызовите исключение KeyError.

Если один из параметров не является строкой, то вызовите исключение TypeError.

Обработка данных должна происходить в порядке: фамилия, имя, имя пользователя.

Если поле заполнено верно, функция возвращает словарь с данными пользователя.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))

Вывод:
{'last_name': 'Иванов', 'first_name': 'Иван', 'username': 'ivanych45'}
"""

class CyrillicError(Exception):
    pass 


class CapitalError(Exception):
    pass 


class BadCharacterError(Exception):
    pass 


class StartsWithDigitError(Exception):
    pass 


def user_validation(**kwargs):
    try:
        if len(kwargs) != 3:
            raise KeyError
        if not all(isinstance(val, str) for val in kwargs.values()):
            raise TypeError
        last_name = kwargs.get('last_name')
        first_name = kwargs.get('first_name')
        username = kwargs.get('username')
        if not all(i.casefold() in set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for i in last_name):
            raise CyrillicError
        if last_name != last_name.title() or any(i.isupper() for i in last_name if i != last_name[0]):
            raise CapitalError
        if not all(i.casefold() in set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for i in first_name):
            raise CyrillicError
        if first_name != first_name.title() or any(i.isupper() for i in first_name if i != first_name[0]):
            raise CapitalError
        if not all(i.casefold() in set("abcdefghijklmnopqrstuvwxyz1234567890_") for i in username):
            raise BadCharacterError
        if username[0].isdigit():
            raise StartsWithDigitError
    except KeyError:
        return "Вызвано исключение KeyError"
    except TypeError:
        return "Вызвано исключение TypeError"
    except CyrillicError:
        return "Вызвано исключение CyrillicError"
    except CapitalError:
        return "Вызвано исключение CapitalError"
    except BadCharacterError:
        return "Вызвано исключение BadCharacterError"
    except StartsWithDigitError:
        return "Вызвано исключение StartsWithDigitError"
    return {"last_name": last_name, "first_name": first_name, "username": username}


print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45", password="123456"))
print(user_validation(last_name="Иванов", first_name="Иван", username="ivanych45"))
