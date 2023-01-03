# Можно использовать функции из других файлов. Запишем функцию тут, а в следующем файле func2.py используем ее
def func(x):
    if x == int(x):
        return "Целое"
    elif x == float(x):
        return "Вещественное"
    else:
        return