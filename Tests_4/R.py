"""
НЕ РЕШЕНА ПРАВИЛЬНО!!!

Новогоднее настроение 2.0
Коллеги математика вновь хотят порадовать его и сделать математические ёлки, которые украсят кабинет учёного.
Помогите им, написав программу, которая по введённому числу строит математическую ёлку.

Формат ввода
Вводится одно натуральное число — количество чисел в математической ёлке.

Формат вывода
Требуемая новогодня ёлка.

Примечание
Не забывайте про существование f-строк.

В данный момент визуализация примеров работает не корректно.

Ввод:
14

Вывод:

     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14
"""

n = int(input())
m = (-1 + (1 + 8 * n) ** 0.5) / 2
m = int(-1 * m // 1 * -1)

c = 0
elka = [[0] * i for i in range(1, m + 1)]

for i in range(m):
    for j in range(0, i + 1):
        if c < n:
            c += 1
            elka[i][j] = c
        else:
            elka[-1].remove(0)

max_len = len(str(' '.join(map(str, elka[-1]))))


for row in elka:
    print('{:^{width}}'.format((' '.join(map(str, row))), width=max_len))


