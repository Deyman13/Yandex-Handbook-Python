"""
Таблица истинности 2

Продолжим работу с таблицами истинности. Продумайте программу, которая для введённого сложного 
логического высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных валидное для языка Python.

Формат вывода
Выведите таблицу истинности данного выражения.

Примечание
В выражении все переменные заданы заглавными латинскими буквами.
Обратите внимание на параметры __globals и __locals у функции eval.

Ввод:
not A or B and C

Вывод:
A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 0
1 0 1 0
1 1 0 0
1 1 1 1
"""

string = input().split()

# узнаем какие буквы были введены, и сколько
letters = sorted({let for let in string if let.isupper()})
max_letters = len(letters)
dct = {}

print(" ".join(letters), "F")

for n in range(0, 2 ** max_letters):
    num = bin(n)
    num = num.replace('b', '0')
    temp = max_letters if max_letters <= 3 else len(num)
    for let in letters:
        dct[let] = int(num[-temp])
        temp -= 1
    if "A" in dct.keys():
        A = dct["A"]
    if "B" in dct.keys():
        B = dct["B"]
    if "C" in dct.keys():
        C = dct["C"]
    if "D" in dct.keys():
        D = dct["D"]
    if "E" in dct.keys():
        E = dct["E"]
    if "G" in dct.keys():
        G = dct["G"]
    if "F" in dct.keys():
        F = dct["F"]
    if "H" in dct.keys():
        H = dct["H"]
    if "I" in dct.keys():
        I = dct["I"]
    if "J" in dct.keys():
        J = dct["J"]
    if "K" in dct.keys():
        K = dct["K"]
    if "L" in dct.keys():
        L = dct["L"]
    if "M" in dct.keys():
        M = dct["M"]
    if "N" in dct.keys():
        N = dct["N"]
    if "O" in dct.keys():
        O = dct["O"]
    if "P" in dct.keys():
        P = dct["P"]
    if "Q" in dct.keys():
        Q = dct["Q"]
    if "R" in dct.keys():
        R = dct["R"]
    if "S" in dct.keys():
        S = dct["S"]
    if "T" in dct.keys():
        T = dct["T"]
    if "U" in dct.keys():
        U = dct["U"]
    if "V" in dct.keys():
        V = dct["V"]
    if "W" in dct.keys():
        W = dct["W"]
    if "X" in dct.keys():
        X = dct["X"]
    if "Y" in dct.keys():
        Y = dct["Y"]
    if "Z" in dct.keys():
        Z = dct["Z"]
    f = 1 if eval(" ".join(string)) else 0
    print(" ".join([str(i) for i in dct.values()]), f'{f}')
