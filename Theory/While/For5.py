# Обратите внимание: изменение значения итерируемой переменной внутри тела цикла не имеет смысла, 
# так как будет перезаписано на следующей итерации очередным значением из диапазона функции range(). 
# Например, следующий код по-прежнему выведет числа от 0 до n - 1, 
# несмотря на изменение значения итерируемой переменной в теле цикла:

n = int(input("Введите n: "))
for i in range(n):
    print(i)
    i = 100 # бессмысленное изменение, оно не будет работать.