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

number = int(input())
temp = 1
max_count_numbers = 1
nowcounter = 0
length = 5
while temp <= number:
    if nowcounter == 0:
        print(" " * length, temp, end=' ')
    else: 
        print(temp, end=" ")
    temp += 1
    nowcounter += 1
    if nowcounter == max_count_numbers:
        print()
        max_count_numbers += 1
        nowcounter = 0
        length -= 1

