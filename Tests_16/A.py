"""
Математика — круто, но это не точно

Давайте вспомним начало нашего задачника, когда всё было просто: мы не использовали ни циклы, ни коллекции, ни объектно-ориентированное программирование. Перед нами были только входные данные и требовалось предоставить результат.

Напишите программу, которая вычисляет значение функции:

f(x) = log32x^3/16 + x^cos(pi*x/2*e) - sin^2 x/pi
 
Формат ввода
Вводится действительное число xx

Формат вывода
Одно число — значение функции в заданной точке.

Ввод:
2.71

Вывод:
0.4818035253577275
"""
from math import log, pow, cos, e, pi, sin

def f(x):
    return log(pow(x, 3/16), 32) + pow(x, cos((pi * x) / (2 * e))) - sin(x / pi) ** 2

print(f(float(input())))
