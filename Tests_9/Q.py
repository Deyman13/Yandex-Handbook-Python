"""
Прятки

Стеганография — способ передачи или хранения информации с учётом сохранения в тайне самого факта 
такой передачи (хранения).

В отличие от криптографии, которая скрывает содержимое тайного сообщения, стеганография скрывает 
сам факт его существования. Как правило, сообщение будет выглядеть как что-либо иное, например, 
как изображение, статья, список покупок, письмо или судоку. Стеганографию обычно используют 
совместно с методами криптографии, таким образом, дополняя её.

Нам был дан файл со скрытым текстом. И было сообщено, что для выделения полезной информации, 
нужно из каждого кода символа в тексте «выдернуть» последние два байта. Это и будет код символа 
полезной информации.
Однако есть одно «но». Если код символа меньше 128 — это и есть полезная информация.

Разработайте программу, которая из текстового файла выделяет полезную информацию.

Формат ввода
В файле secret.txt хранится текст.

Формат вывода
Выведите спрятанное сообщение.

Примечание
Для манипуляции кодами символов изучите работу функций chr и ord.

Ввод:
᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!

Вывод:
Hello, world!
"""

# Открываем файл с текстом для чтения
with open("secret.txt", "r") as f:
    # Считываем содержимое файла
    text = f.read()

for letter in text:
    ord_letter = ord(letter)
    if ord_letter > 128:
        symbol_bin = bin(ord(letter))
        new_sym = symbol_bin[-8:]
        print(chr(int(f"{new_sym}", 2)), end="")
    else:
        print(chr(ord_letter), end="")

    


    
    


