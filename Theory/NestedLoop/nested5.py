# В циклах while и for можно использовать оператор else.
# Записанный в нём код будет выполняться, когда для цикла while нарушится условие продолжения, а для цикла for
# закончатся итерации. Напишем программу, которая будет считывать строки, пока пользователь не введёт «СТОП»:

#while input("Введите строку (СТОП для остановки): ") != "СТОП":
#    pass
#else:
#    print("Цикл завершён")

# После завершения цикла сработает оператор else, и код внутри него выведет строку «Цикл завершён».
# Оператор break влияет на поведение оператора else в циклах. Если в цикле сработал оператор break, то цикл сразу 
# завершается, а код в операторе else выполняться не будет. Перепишем предыдущий пример, добавив проверку: если 
# введённое значение равно "ignore_else", то остановим цикл с помощью break:

while (text := input("Введите строку (СТОП для остановки): ")) != "СТОП":
    if text == "ignore_else":
        break
else:
    print("Цикл завершён")

# Когда пользователь введёт «СТОП», цикл попадёт в блок else, и в терминале появится строка «Цикл завершён». 
# А при вводе "ignore_else" сработает оператор break, и цикл завершится, не выполняя код в else.

