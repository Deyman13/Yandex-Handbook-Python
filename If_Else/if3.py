print("Введите первую и последнюю буквы русского алфавита.")
first_letter = input()
last_letter = input()
if (first_letter == "а" or first_letter == "А") and ( # Если первая буква равна а или А и при этом
        last_letter == "я" or last_letter == "Я"): # Последняя буква равна я или Я то:
    print("Верно.") 
else: # Иначе это: 
    print("Неверно.")
