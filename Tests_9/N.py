"""
Слияние данных

Одна местная компания производит обновление данных о пользователях и заодно произвести реорганизацию системы хранения.

Напишите программу, которая обновляет данные о пользователях, записанных в JSON файле.

Формат ввода
Пользователь вводит два имени файла.
В первом хранится JSON массив пользователей.
Во втором — массив новых данных.

Информация о каждом пользователе представляется JSON объектом, в котором обязательно присутствует поле name, 
описывающее имя пользователя. Остальные поля являются дополнительными.

Формат вывода
В первый файл запишите информацию о пользователях в виде JSON объекта, ключами которого выступают имена пользователей, 
а значениями — объекты с информацией о них.

Если какая-либо дополнительная информация о пользователе изменяется, то требуется сохранить лексикографически 
большее значение.

Ввод:
# Пользовательский ввод:
users.json
updates.json

# Содержимое файла users.json
[
    {
        "name": "Ann",
        "address": "Flower st."
    },
    {
        "name": "Bob",
        "address": "Summer st.",
        "phone": "+7 (123) 456-78-90"
    }
]

# Содержимое файла updates.json
[
    {
        "name": "Ann",
        "address": "Awesome st.",
        "phone": "+7 (098) 765-43-21"
    },
    {
        "name": "Bob",
        "address": "Winter st."
    }
]

Вывод:
# Содержимое файла users.json
{
    "Ann": {
        "address": "Flower st.",
        "phone": "+7 (098) 765-43-21"
    },
    "Bob": {
        "address": "Winter st.",
        "phone": "+7 (123) 456-78-90"
    }
}
"""

import json

users = input()
updates = input()

with open(users) as f:
    old_data = json.load(f)

with open(updates) as f:
    new_data = json.load(f)

# Создаем пустой словарь
updated_data = {}

# Итерируемся по старым данным
for old_user in old_data:
    # Имени присваиваем значение ключа name в словаре
    name = old_user['name']
    # Создаем ключ в словаре, значением которого поставим пустой словарь
    updated_data[name] = {}
    # Итерируемся по новым данным
    for new_user in new_data:
        # Если значение ключа name равен имени
        if new_user['name'] == name:
            # Итерируемся по ключам и значением словаря
            for key, value in new_user.items():
                # Если ключ так же имеется и в старых данных
                if key in old_user:
                    # Сравниваем лексикографически значения ключей
                    if old_user[key] < value:
                        # В случае, если меньше - присваиваем
                        old_user[key] = value
                # Если запись не содержится в старом словаре, то просто присваиваем новую запись
                else:
                    old_user[key] = value
    # Итерируемся по ключам и значениям старого словаря
    for key, value in old_user.items():
        # Если ключ не name
        if key != 'name':
            # то присваиваем все значения вне словаря в пустой словарь, тем самым делаем только ключ, как имя
            # и значение, как все остальное. 
            updated_data[name][key] = value

with open(users, 'w') as f:
    json.dump(updated_data, f, ensure_ascii=False, indent=4)










