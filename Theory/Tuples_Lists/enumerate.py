# Если требуется совместить проход непосредственно по символам строки с определением индекса итерации, то можно 
# воспользоваться функцией enumerate. Она возвращает пары значений — номер элемента коллекции и сам этот элемент. 
# Эта функция удобна, когда нужно пройти именно по элементам коллекции, но при этом ещё и знать индекс каждого элемента.
text = input()
for i, letter in enumerate(text):
    print(f"{i}. {letter}")

