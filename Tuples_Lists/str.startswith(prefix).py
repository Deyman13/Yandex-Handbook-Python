# Метод	str.startswith(prefix)
# Описание	Возвращает True, если строка начинается на подстроку prefix, иначе возвращает False. 
# prefix может быть кортежем проверяемых префиксов строки. Под кортежами подразумевается неизменяемая
# последовательность элементов
s = "Hello, world!"
print(s.startswith("Hello"))
s = "Hello, world!"
print(s.startswith("Bye"))
# Результат	True, False

