"""
Частотный анализ на минималках

Частотный анализ — подсчёт, какие символы чаще всего встречаются в тексте. 
Это важнейший инструмент взлома многих классических шифров — от шифра Цезаря и до шифровальной машины «Энигма». 
Выполним простой частотный анализ: выясним, какой символ встречается в тексте чаще всего.

Формат ввода
Вводятся строки, пока не будет введена строка «ФИНИШ».

Формат вывода
Выводится один символ в нижнем регистре — наиболее часто встречающийся.

Примечания
Пробелы в анализе не участвуют.
Если в результате анализа получено несколько ответов, следует вывести первый по алфавиту.

Ввод:
Баобаб
Белка
Бобы
ФИНИШ

Вывод:
б
"""

answer = "" 
counter = 0 
dct = {}
while True:
    temp = input()
    n = temp.upper()
    for now in n:
        if now not in dct:
            dct[now] = 0
        dct[now] += 1
    for key in dct:
        if key != " ":
            if dct[key] > counter:
                counter = dct[key]
                answer = key
            elif dct[key] == counter:
                if key < answer:
                    answer = key 
    if temp == "ФИНИШ":
        break
print(answer.lower())

