# Для удаления элемента из списка применяется операция del. Нужно указать индекс элемента, который требуется удалить:

numbers = [10, 20, 50]
del numbers[-1]
print(numbers)

# С помощью del можно удалить несколько элементов списка. Для этого вместо одного элемента указываем срез:

numbers = [1, 2, 3, 4, 5]
del numbers[::2]
print(numbers)