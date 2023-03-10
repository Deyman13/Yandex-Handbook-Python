"""
А есть ещё варианты?
Давайте вновь поможем Виталию выяснить, какие вариации вытащить из колоды определённые тройки карт возможны. 
Напишите программу, которая выводит список вариантов согласно требованиям.

Формат ввода
В первой строке записана масть, которая должна присутствовать в тройке. Во второй строке записан достоинство, 
которого не должно быть в тройке. В третьей строке записан предыдущий вариант полученный Виталием.

Формат вывода
Выведите следующий вариант расклада.

Примечание
Обратите внимание: валет-дама-король-туз лексикографически упорядочены. Но «10 ...» лексикографически младше, 
чем «2 ...», а бубны младше, чем пики.

Масти в именительном и родительном падежах:

Именительный	Родительный
буби	        бубен
пики	        пик
трефы	        треф
черви	        червей

Ввод
пики
10
9 пик, король треф, туз червей

Вывод
9 пик, король червей, туз бубен
"""

from itertools import chain

suits_change = ["бубен", "пик", "треф", "червей", "бубен"]

advantages_of_the_card = list(chain(sorted([str(i) for i in range(2, 11)]), ["валет", "дама", "король", "туз"]))

selected_suits = input()

selected_adv = input()

lv = input().split(", ")
first_card = lv[0].split()
second_card = lv[1].split()
third_card = lv[2].split()

f_card = [first_card[0], " ", first_card[1]]
idx = suits_change.index(second_card[1])
sec_card = [second_card[0], " ", suits_change[idx + 1]]

idx2 = suits_change.index(third_card[1])
th_card = [third_card[0], " ", suits_change[idx2 + 1]]

cards = list(chain(f_card, ", ", sec_card, ", ", th_card))
print("".join(str(i) for i in cards))





