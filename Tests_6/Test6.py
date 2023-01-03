"""
Кашееды — 3
Вернёмся к условию, когда каждый воспитанник детского сада любит либо манную, либо овсяную, либо обе эти каши.
Напишите программу, которая позволит воспитателю узнать, какие дети любят только одну кашу.

Формат ввода
В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
Затем идут N + M строк — перемешанные фамилии детей.
Гарантируется, что в группе нет однофамильцев.

Формат вывода
В алфавитном порядке фамилии учеников, которые любят только одну кашу.
Если таких не окажется, в строке вывода нужно написать «Таких нет».

Ввод:
3
2
Васильев
Петров
Васечкин
Иванов
Михайлов

Вывод:
Васечкин
Васильев
Иванов
Михайлов
Петров

Решение: Записываем фамилии N + M раз, проверяем фамилию на наличии во множестве, если она уже в нем, удаляем ее, иначе добавляем.
Проверяем, есть ли во множестве фамилии при помощи len(), если есть - выводим, иначе "Таких нет"
"""

N = int(input())
M = int(input())
set_1 = set()
for i in range(N + M):
    secondname = input()
    if secondname not in set_1:
        set_1.add(secondname)
    else:
        set_1.remove(secondname)
if len(set_1) > 0:
    for x in sorted(set_1):
        print(x)
else:
    print("Таких нет")
