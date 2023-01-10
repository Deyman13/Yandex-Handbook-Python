"""
Найдётся всё 3.0

Давайте вновь напишем небольшой компонент поисковой системы.

Формат ввода
Сначала вводится поисковый запрос.
Затем вводятся имена файлов, среди которых следует произвести поиск.

Формат вывода
Выведите все имена файлов, в которых есть поисковая строка без учета регистра и повторяющихся пробельных символов.
Если ни в одном файле информация не была найдена, выведите "404. Not Found".

Примечание
Система поиска должна обрабатывать строки "a&nbsp;&nbsp;&nbsp;&nbsp;b", "a b" и "a\nb" как одинаковые.

Ввод
# Пользовательский ввод:
Мама мыла РАМУ
first.txt
second.txt

# Содержимое файла fist.txt
В этом файле говорится    о том что МАМА   

мылА
Раму

# Содержимое файла second.txt
А в этом не говорится

Вывод
first.txt
"""

import sys

def normalize_string(string):
    # Убираем все ненужные символы из строки
    return ' '.join(string.replace("&nbsp;&nbsp;&nbsp;&nbsp;", " ").replace("\n", " ").split())


# Поисковой запрос и имена файлов
query = input().casefold().split()
filenames = []
for line in sys.stdin:
    filenames.append(line.strip())

# Получить все строки из всех файлов
contents = []
for filename in filenames:
    with open(filename, 'r', encoding="utf-8") as file:
        contents.append(file.read())

# Получить совпадения, если они есть
results = set()
for index, line in enumerate(contents):
    line = normalize_string(line)
    line_split = line.casefold().split()
    count = 0
    for word in query:
        for w in line_split:
            if word == w:
                count += 1
            if count == len(query):
                results.add(index)

# Вывести результат, если список совпадений не пустой. 
if results:
    for result in results:
        print(filenames[result])
else:
    print("404. Not Found")



