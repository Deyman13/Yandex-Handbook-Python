# Благодаря словарям нашу программу можно переписать, используя в качестве ключей словаря названия стран, 
# а в качестве значений по ключам — названия столиц этих стран:

countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
print(countries_and_capitals["Франция"])

# Как видно из программы, для создания словаря можно перечислить в фигурных скобках пары: ключ и значение. 
# Ключ и значение отделяются двоеточием и пробелами, а пары перечисляются через запятую.

# В качестве ключей можно использовать значения неизменяемого типа: числа, строки, кортежи. 
# Значения по ключу могут быть любого типа данных.

# Чтобы взять значение по ключу, необходимо указать ключ в квадратных скобках после имени словаря.

# Если же нужно добавить новый ключ в словарь, то его указывают после имени словаря в левой части операции присваивания, а
# значение, которое будет храниться по этому ключу, — в правой части:
countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
countries_and_capitals["Сербия"] = "Белград"
print(countries_and_capitals)

# Обратите внимание, при записи значения по уже существующему ключу он создаётся заново с новым значением, а прошлый стирается:

d = {"key": "old_value"}
d["key"] = "new_value"
print(d["key"])


