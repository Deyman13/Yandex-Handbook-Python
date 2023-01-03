# При попытке взять значение по несуществующему ключу происходит исключение KeyError:

# countries_and_capitals = {"Россия": "Москва",
#                          "США": "Вашингтон",
#                          "Франция": "Париж"}
# print(countries_and_capitals["Сербия"])
# KeyError

# Для проверки существования ключа в словаре следует использовать уже известный нам оператор in:

countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
if "Сербия" in countries_and_capitals:
    print(countries_and_capitals["Сербия"])
else:
    print("Страна пока не добавлена в словарь")

# По ключам в словаре можно пройти в цикле for:

countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
for country in countries_and_capitals:
    print(f"У страны {country} столица — {countries_and_capitals[country]}.")

