"""
Расклад таков...

Виталий любит играть в карты. Он решил выяснить, какие есть вариации вытащить из колоды определённые тройки карт. 
Напишите программу, которая выводит список вариантов согласно требованиям.

Формат ввода
В первой строке записана масть, которая должна присутствовать в тройке.
Во второй строке записан достоинство, которого не должно быть в тройке.

Формат вывода
Выведите на экран первые 10 получившихся троек.
Карты в каждой комбинации должны быть отсортированы лексикографически (по строке названия карты). 
Карты комбинации выводятся через запятую с пробелом после неё.
Комбинации между собой также должны быть отсортированы в лексикографическом порядке по строке, представляющей комбинацию целиком.

Примечание
Обратите внимание: валет-дама-король-туз лексикографически упорядочены. Но «10 ...» лексикографически младше, 
чем «2 ...», а бубны младше, чем пики.

Масти в именительном и родительном падежах:

Именительный	Родительный
буби	        бубен
пики	        пик
трефы	        треф
черви	        червей

Ввод:
пики
10

Вывод:
2 бубен, 2 пик, 2 треф
2 бубен, 2 пик, 2 червей
2 бубен, 2 пик, 3 бубен
2 бубен, 2 пик, 3 пик
2 бубен, 2 пик, 3 треф
2 бубен, 2 пик, 3 червей
2 бубен, 2 пик, 4 бубен
2 бубен, 2 пик, 4 пик
2 бубен, 2 пик, 4 треф
2 бубен, 2 пик, 4 червей

Решение: Поступает масть в именительном падеже, нам необходимо ее заменить на идентичную, но родительного падежа. 
Объединить все достоинства карты от 2 до туза при помощи chain(), для замены масти используем index(), и присваиваем
по такому же индексу, но уже в списке родильного падежа, масть. Так же поступает ненужное достоинство, его мы просто
удаляем из списка достоинств. Объединяем масти и достоинства с помощью production()
Мутируем список при помощи permutations(), в аргументы передаем уже объединенные масти и достоинства, а так же
то, какие комбинации нам нужны (это 3 в нашем случае) и сортируем его sorted(). Создаем временную переменную,
как условный счетчик и будем увеличивать его на каждой итерации цикла. Запускаем цикл for, с условием "если
временная переменная не равна 10", так как нужно вывести всего 10 первых комбинаций, а не тысячи. Проверяем есть ли
нужная масть в комбинации, и если есть - выводим строку комбинации, используя генераторы списков и строк. 
"""

from itertools import product, chain, permutations

suits = ["буби", "пики", "трефы", "черви"]
suits_change = ["бубен", "пик", "треф", "червей"]

advantages_of_the_card = list(chain(sorted([str(i) for i in range(2, 11)]), ["валет", "дама", "король", "туз"]))

selected_suits = input()
index_suits = suits.index(selected_suits)
selected_suits = suits_change[index_suits]

selected_adv = input()
advantages_of_the_card.remove(selected_adv)

cards = product(advantages_of_the_card, suits_change)

mutations = sorted(permutations(cards, 3))

temp = 0
for value in mutations:
    if temp != 10:
        for i in value:
            if selected_suits in i:
                print(", ".join([str(" ".join(i)) for i in value]))
                temp += 1
                break
    
