"""
Кофейня

Руководство местной кофейни для программистов под названием Java-0x00 решило модернизировать систему заказа кофе.

Для этого им требуется реализовать функцию order, которая принимает список предпочтений посетителя в 
порядке «убывания желания».

Согласно положению, каждый напиток в кофейне строго определён рецептом:

Эспрессо готовится из: 1 порции кофейных зерен.
Капучино готовится из: 1 порции кофейных зерен и 3 порций молока.
Макиато готовится из: 2 порций кофейных зерен и 1 порции молока.
Кофе по-венски готовится из: 1 порции кофейных зерен и 2 порций взбитых сливок.
Латте Макиато готовится из: 1 порции кофейных зерен, 2 порций молока и 1 порции взбитых сливок.
Кон Панна готовится из: 1 порции кофейных зерен и 1 порции взбитых сливок.
В глобальной переменной in_stock содержится словарь, описывающий ингредиенты в наличии. 
Ключи словаря: coffee, cream, milk.

Функция должна вернуть:

название напитка, который будет приготовлен;
сообщение «К сожалению, не можем предложить Вам напиток», если ни одно из предпочтений не может быть приготовлено.
Если заказ, может быть совершён, количество доступных ингредиентов должно соответствующим образом уменьшиться.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
in_stock = {"coffee": 1, "milk": 2, "cream": 3}
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))

Вывод:
Эспрессо
К сожалению, не можем предложить Вам напиток
"""

def order(*preferences):
    temp = "К сожалению, не можем предложить Вам напиток"
    for coffee in preferences:
        if coffee not in result or any([c in result for c in preferences]):
            if coffee == "Эспрессо" and in_stock["coffee"] > 0:
                in_stock["coffee"] -= 1
                result.append(coffee)
                temp = coffee
                break
            elif coffee == "Капучино" and in_stock['coffee'] > 0 and in_stock['milk'] > 2:
                in_stock['coffee'] -= 1
                in_stock['milk'] -= 3
                result.append(coffee)
                temp = coffee
                break
            elif coffee == "Макиато" and in_stock["coffee"] > 1 and in_stock["milk"] > 0:
                in_stock["coffee"] -= 2
                in_stock["milk"] -= 1
                result.append(coffee)
                temp = coffee
                break
            elif coffee == "Кофе по-венски" and in_stock["coffee"] > 0 and in_stock["cream"] > 1:
                in_stock["coffee"] -= 1
                in_stock["cream"] -= 2
                result.append(coffee)
                temp = coffee
                break
            elif coffee == "Латте Макиато" and in_stock["coffee"] > 0 and in_stock["milk"] > 1:
                if in_stock["cream"] > 0:
                    in_stock["coffee"] -= 1
                    in_stock["milk"] -= 2
                    in_stock["cream"] -= 1
                    result.append(coffee)
                    temp = coffee
                    break
            elif coffee == "Кон Панна" and in_stock["coffee"] > 0 and in_stock["cream"] > 0:
                in_stock["coffee"] -= 1
                in_stock["cream"] -= 1
                result.append(coffee)
                temp = coffee
                break
    if len(result) == 6 or all([c in result for c in preferences]):
        result.clear()
    return temp


result = []

in_stock = {"coffee": 1, "milk": 2, "cream": 3}
