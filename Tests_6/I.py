"""
Зайка — 9

Поможем детям подсчитать, сколько за окном поезда встречается животных и деревьев каждого вида.

Формат ввода
В каждой строке записано описание придорожной местности.
Конец ввода обозначается пустой строкой.

Формат вывода
Список увиденного и их количество.
Порядок вывода не имеет значения.

Ввод:
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка

Вывод:
березка 2
елочка 2
зайка 3
волк 1
сосна 6
медведь 1
белочка 2

Решение: Создаем пустой словарь. Запускаем бесконечный цикл, который будет работать, пока не будет введена пустая
строка, в цикле каждую строку разбиваем на слова. Каждое слово проверяем на наличие в словаре. Если его еще нет, то слово будет
являться новым ключом, и к нему присваиваем значение 0, на следующем шаге добавляем + 1 к значению. В случае если слово уже
имеется в словаре, то пропускаем шаг с созданием нового ключа, и просто добавляем + 1 к значению. После завершения цикла
обращаемся к ключам и значениям одновременно при помощи .items() и если ключ не пустая строка (пустая строка запишется последней,
она нужна для завершения цикла) то выводим ключ и его значение.
"""

dct = {}
while True:
    rabbit = input()
    temp = rabbit.split(" ")
    for r in temp:
        if r not in dct:
            dct[r] = 0
        dct[r] += 1
    if rabbit == "":
        break
for key, value in dct.items():
    if key != "":
        print(key, value)
