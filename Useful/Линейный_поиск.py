names = ["Антон", "Валерий", "Женя", "Евгений", "Лера", "Оля", "Таня", "Кира"]
search_for = "Антон" # То, что ищем

def linear_search(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0] # если нашли, то возвращаем индекс
    return None # если ничего не нашли

print(f"{search_for} найден под индексом: {linear_search(names, search_for)}")

# Довольно медленный вид поиска



