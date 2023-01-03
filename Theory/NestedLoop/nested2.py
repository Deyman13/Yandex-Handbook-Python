# Циклы for и while можно останавливать при наступлении определённого условия. 
# Для этого используется оператор break.

# Рассмотрим следующий пример:

password = "right_password"
while True:
    if input("Введите пароль: ") == password:
        print("Пароль принимается")
        break

# В примере мы запускаем бесконечный цикл, в котором просим пользователя ввести пароль и сравниваем результат с 
# верным паролем. В случае если введённый пароль совпал с верным, то выводим фразу «Пароль принимается» и останавливаем цикл.