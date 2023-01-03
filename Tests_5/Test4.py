"""
Очистка данных
Местный провайдер собирает большое количество логов, однако зачастую файлы с отчётами приходят в негодность.
Самые частые проблемы — ошибки вида ## и @@@.
Напишите программу, которая избавляется от:

Двух символов # в начале информационных сообщений;
Строк, заканчивающихся тремя символами @.
Формат ввода
Вводятся строки отчёта. Признаком завершения ввода считается пустая строка.

Формат вывода
Очищенные данные.

Ввод:
Hello, world
Hello, @@@
##Goodbye

Вывод:
Hello, world
Goodbye
"""

list_temp = []
while True: # бесконечный цикл в котором все, что мы будем вписывать в терминал, попадет в список list_temp
    temp = input()
    list_temp.append(temp)
    if temp == "": # если введена пустая строка, остановить цикл
        break
del list_temp[-1] # удаляем последний элемент, так как это пустая строка
new_list = []
for string in list_temp:
    if string[0] == "#" and string[1] == "#" and string[-1] != "@": # если первые 2 элемента это #, то удалим их lstrip
        new_list.append(string.lstrip("#"))
    elif string[-1] != "@" and string[-2] != "@" and string[-3] != "@": # если последние элементы не @, оставляем как есть
        new_list.append(string)
for i in range(len(new_list)): 
    print(new_list[i]) # выводим полученные очищенные строки