# В Python версии 3.8 появился моржовый оператор (walrus operator). Он записывается как := и позволяет одновременно 
# вычислить выражение, присвоить результат переменной и вернуть это значение, например в условие.
# Давайте напишем программу, которая будет здороваться со всеми людьми, чьи имена введёт пользователь. 
# Сигнал для остановки — ввод строки «СТОП»:

name = input("Введите имя: ")
while name != "СТОП":
    print(f"Привет, {name}!")
    name = input("Введите имя: ")
print("Программа завершена.")

# А теперь перепишем эту программу с использованием моржового оператора:

while (name := input("Введите имя: ")) != "СТОП":
    print(f"Привет, {name}!")
print("Программа завершена.")

# Благодаря моржовому оператору из программы были убраны строки, в которых считывалось имя первый раз до цикла, а также в теле цикла. 
# Теперь имя считывается только непосредственно на этапе проверки, выполняется ли условие продолжения цикла.

# Итак, цикл while обычно применяется в тех случаях, когда заранее не известно, сколько итераций будет выполнено, 
# но известно условие, при котором цикл продолжает работу.
