"""
Кашееды

Каждый воспитанник детского сада любит либо манную, либо овсяную, либо обе каши.
Давайте создадим программу, которая позволит воспитателю быстро выяснить, сколько детей любят обе каши.

Формат ввода
В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
Затем идут N строк — фамилии детей, которые любят манную кашу, и M строк с фамилиями детей, любящих овсяную кашу.
Гарантируется, что в группе нет однофамильцев.

Формат вывода
Количество учеников, которые любят обе каши.
Если таких не окажется, в строке вывода нужно написать «Таких нет».

Пример 1                    Пример 2                

Ввод:                       Ввод:
3                           3
2                           3
Васильев                    Иванов
Петров                      Петров
Васечкин                    Васечкин
Иванов                      Иванов
Михайлов                    Петров
                            Васечкин

Вывод:                      Вывод:
Таких нет                   3


Решение:
Для каждой группы детей, в зависимости от их предпочтения по каше мы записываем фамилии. Количество детей в списке любителей
определенной каши определяется значениями N и M. Записываем уникальные фамилии в список путем проверки, нет ли в
нашем списке уже этой фамилии. С первой кашей - записываем всех, со второй уже проверяем, и в случае, если фамилия
уже присутствует в списке то добавляем + 1 к условному счетчику. Выводим счетчик если он не нулевой, иначе "Таких нет"
"""
N = int(input())
M = int(input())
result = [] 
counter = 0 
for i in range(N): 
    secondname = input()  
    result.append(secondname) 
for i in range(M): 
    secondname = input() 
    if secondname not in result: 
        result.append(secondname) 
    else:
        counter += 1 
print(counter if counter > 0 else "Таких нет") 



        

