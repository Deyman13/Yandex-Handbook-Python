# В упорядоченных коллекциях, к которым относится строка, каждое значение автоматически имеет свой номер — индекс.
# Индексация в коллекциях Python начинается со значения 0. При этом пробел, запятая, управляющие символы \n, \t и прочие тоже
# получают свой индекс в строке. 
# Для доступа к определённому символу строки по индексу нужно указать его в квадратных скобках сразу после имени переменной.

# Давайте создадим программу, которая выводит первый символ строки, введённой пользователем:

text = input()
print(text[0])

# Если пользователь введёт пустую строку, то наша программа выдаст ошибку:
# IndexError: string index out of range

# В пустой строке нет символов, и программа вышла за пределы строки. Таким образом, нельзя получить значение по индексу, 
# который за пределами строки. Перед обращением к символу строки по индексу можно проверять, не выходит ли он за пределы 
# строки, используя известную нам функцию len следующим образом:

text = input("Введите строку: ")
i = int(input("Введите индекс символа: "))
if i < len(text):
    print(text[i])
else:
    print("Индекс выходит за пределы строки")
    