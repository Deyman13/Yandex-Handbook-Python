"""
Кашееды — 4
Каждый воспитанник детского сада любит одну или несколько каш.
Поможем воспитателю составить список детей, которые любят конкретную кашу.

Формат ввода
В первой строке задаётся количество детей в группе (NN). В следующих NN строках записана фамилия ребенка и список его любимых каш.
В последней строке записана каша, информацию о которой хочет получить воспитатель.

Формат вывода
Фамилии учеников, которые любят заданную кашу, в алфавитном порядке.
Если таких не окажется, в строке вывода нужно написать «Таких нет».

Ввод:
5
Васильев манная
Петров манная
Васечкин манная
Иванов овсяная
Михайлов овсяная
манная

Вывод:
Васечкин
Васильев
Петров

Решение: Создаем пустой словарь, в которым будем записывать ключи - каши, а значения - фамилии. Так как каш может быть несколько
у каждого из учеников, используем срез [1:], тем самым к каждой каше мы добавим значение фамилии. Перебираем по срезу каши
и каждую проверяем на наличие в словаре. Если ее еще нет в словаре, то записываем ее как ключ, а как значение используем фамилию. 
Если она уже есть в словаре, то просто добавляем к ней еще одну фамилию. Введенная в последнюю очередь каша будет являться ключом
по которому нужно будет выдать значения. Проверяем ее наличие в словаре, если она имеется, записываем все значения в пустой список
и выводим все фамилии из него. Если каши в словаре нет, то выводим "Таких нет".
"""


N = int(input())
kasha = dict()
for i in range(N):
    secondname = input().split(" ")
    name = secondname[0]
    kasha_keys = secondname[1:]
    for each in kasha_keys:
        if each not in kasha:
            kasha[each] = [name]
        else:
            kasha[each].append(name)
selected_kasha = input()
answer = []
if selected_kasha in kasha:
    for i in range(len(kasha[selected_kasha])):
        answer.append(kasha[selected_kasha][i])
else:
    print("Таких нет")
for j in sorted(answer):
    print(j)
