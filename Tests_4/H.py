"""
Максимальная сумма

Ребята в детском саду снова играют с числами. И пусть числа они знают плохо, придумывать их они очень любят.
Они договорились, что будут называть числа по очереди и тот, кто назовёт число с наибольшей суммой цифр, будет считаться 
победителем. В качестве судьи они выбрали бедную воспитательницу, и она попросила нас о помощи. Напишите программу, 
которая определит победителя.

Формат ввода
В первой строке записано число N — количество детей в группе. Далее вводятся имя ребенка и его число (каждое на своей строке).

Формат вывода
Требуется вывести имя победителя.
Если два ребенка назвали числа с одинаковой суммой цифр, победителем должен быть признан тот, кто ходил позже.

Ввод:
2
Аня
123
Боря
234

Вывод:
Боря
"""

number = int(input())
maximum = 0
for i in range(number):
    tempname = input() # вводим имя ребенка
    tempnumber = int(input()) # его число
    summa = 0
    while tempnumber != 0: # считаем сумму цифр в числе в цикле
        summa += tempnumber % 10
        tempnumber //= 10
        if summa > maximum: # проверяем на максимум
            maximum = summa
            maxname = tempname
        if summa == maximum:
            maxname = tempname
print(maxname)