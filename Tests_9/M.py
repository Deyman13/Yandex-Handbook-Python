"""
Обновление данных

Часто приходится обновлять данные.

Создайте программу, которая обновляет JSON файл.

Формат ввода
Пользователь вводит имя файла.
Затем вводятся строки вида ключ == значение.

Формат вывода
В заданный пользователем файл следует записать обновленный JSON.

Ввод:
# Пользовательский ввод:
data.json
one == один
two == два
three == три

# Содержимое файла data.json
{
    "one": 1,
    "three": 2
}

Вывод:
# Содержимое файла data.json
{
    "one": "один",
    "three": "три",
    "two": "два"
}
"""

import json

filename = input()

# Открываем файл и загружаем содержимое в data
with open(filename, encoding="utf-8") as f:
    data = json.load(f)

# Считываем строки вида ключ == значение
while True:
    try:
        line = input()
        key, value = line.split(" == ")
        # Обновляем словарь
        data[key] = value
    except EOFError:
        break

# Открываем файл в режиме записи и записываем обновленный словарь
with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

