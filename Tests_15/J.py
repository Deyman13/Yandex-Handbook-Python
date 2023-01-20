"""
Валидация пароля

После того как пользователь ввёл свои данные в требуемом формате, можно позаботиться и о пароле.

Напишите функцию password_validation, которая принимает один позиционный параметр — пароль, и следующие 
именованные параметры:

min_length — минимальная длина пароля, по умолчанию 8;
possible_chars — строка символов, которые могут быть в пароле, по умолчанию латинские буквы и цифры;
at_least_one — функция возвращающая логическое значение, по умолчанию str.isdigit.

Если переданный позиционный параметр не является строкой, вызовите исключение TypeError.

А так же реализуйте собственные исключения:

MinLengthError — вызывается, если пароль меньше заданной длины;
PossibleCharError — вызывается, если в пароле используется недопустимый символ;
NeedCharError — вызывается, если в пароле не найдено ни одного обязательного символа.
Проверка условий должна происходить в порядке указанном в задании.

Так как, хороший разработчик никогда не хранит пароли в открытом виде, функция, в случае успешного 
завершения, возвращает хеш пароля. Для этого воспользуйтесь функцией sha256 из пакета hashlib и верните 
его шестнадцатеричное представление.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
print(password_validation("Hello12345"))

Вывод:
67698a29126e52a6921ca061082783ede0e9085c45163c3658a2b0a82c8f95a1
"""

import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8,
                        possible_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                        at_least_one=str.isdigit):
    try:
        if not isinstance(password, str):
            raise TypeError
        if len(password) < min_length:
            raise MinLengthError
        if not all(i in possible_chars for i in password):
            raise PossibleCharError
        if not any(at_least_one(i) for i in password):
            raise NeedCharError
    except TypeError:
        return "Вызвано исключение TypeError"
    except MinLengthError:
        return "Вызвано исключение MinLengthError"
    except PossibleCharError:
        return "Вызвано исключение PossibleCharError"
    except NeedCharError:
        return "Вызвано исключение NeedCharError"
    return hashlib.sha256(password.encode()).hexdigest()


print(password_validation(
    "$uNri$e_777",
    min_length=6,
    at_least_one=lambda char: char in "!@#$%^&*()_"
))
