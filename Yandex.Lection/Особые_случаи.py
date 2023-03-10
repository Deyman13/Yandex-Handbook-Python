# Сумма последовательности. 
seq = list(map(int, input().split())) # Считывается последовательность чисел введенное в одну строку, режется на символы
# каждый символ отдельно превращается в число и все переходит в список. (чтение последовательности символов)
if len(seq) == 0: # Если длина последовательности = 0, выводим 0
    print(0)
else:
    seqsum = seq[0] # присваиваем сумме нулевой индекс
    for i in range(1, len(seq)):
        seqsum += seq[i] # суммируем и выводим. 
    print(seqsum)

# Модифицируем код
seq = list(map(int, input().split()))
seqsum = 0 # Убрали условие if и присвоили 0, в случае, если последовательность пуста = мы выведем 0
for i in range(len(seq)): # Убрали seqsum = seq[0] так как в диапазоне мы начинаем с 0 индекса, если не указываем другое.
    seqsum += seq[i]
print(seqsum)

# Максимум последовательности
seq = list(map(int, input().split()))
seqmax = 0
for i in range(len(seq)):
    if seq[i] > seqmax:
        seqmax = seq[i]
print(seqmax)
# Не будет работать, когда все числа в последовательности - отрицательные

# Модифицируем код
seq = list(map(int, input().split()))
if len(seq) == 0: # Если последовательность пустая, мы выводим - бесконечность
    print('-inf')
else:
    seqmax = seq[0] # иначе присваиваем индекс 0, чтобы был хоть какой то максимум в любом случае. 
    for i in range(1, len(seq)): # идем с 1 до количества чисел
        if seq[i] > seqmax: # вычисляем максимум и выводим. 
            seqmax = seq[i]
    print(seqmax)


