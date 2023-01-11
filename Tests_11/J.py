"""
Ключевой секрет

Вася любит секреты и шифрование. Он часто пользуется шифром на основе замен и просит разработать вас 
функцию, которая позволит ему быстро шифровать сообщения.

Напишите функцию secret_replace, которая принимает:

текст требующий шифрования;
именованные аргументы — правила замен, представляющие собой кортежи из одного или нескольких значений.
Функция должна вернуть зашифрованный текст.

Примечание
Ваше решение должно содержать только функции.
В решении не должно быть вызовов требуемых функций.

Ввод:
result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))

Вывод:
result = 'Hehiy123, wzrhid!'
"""

def secret_replace(text, **rules):
    keys_replaced = {}
    for key in rules.keys():
        keys_replaced[key] = 0
    i = 0
    temp_len = len(text)
    while i != temp_len:
        if text[i] in rules:
            old_char = text[i]
            if old_char not in keys_replaced:
                keys_replaced[old_char] = 0
            text = text[:i] + rules[old_char][keys_replaced[old_char]] + text[i + 1:]
            keys_replaced[old_char] += 1
            if keys_replaced[old_char] == len(rules[old_char]):
                keys_replaced[old_char] = 0
        i += 1
        temp_len = len(text)
    return text

