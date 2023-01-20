"""
Обработка ошибок

Вашему решению будет предоставлена функция func, которая не имеет параметров и результата. 
Однако во время её исполнения может произойти одна из ошибок: ValueError, TypeError или SystemError.

Вызовите её, обработайте ошибку и выведите её название. Если ошибка не произойдёт, выведите сообщение 
"No Exceptions".

Ввод:
def func():
    x = int('Hello, world!')

Вывод:
ValueError
"""

def func(): # Не прикреплять к тестирующей системе!
    x = int('Hello, world!')

try:
    func()
    print("No Exceptions")
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except SystemError:
    print("SystemError")

