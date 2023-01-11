"""
В эфире рубрика «Эксперименты»

Лаборанты проводят эксперимент и запросили разработку системы обработки данных. 
Результатами эксперимента должны стать пары рациональных чисел.

Для работы им требуются функции:

enter_results(first, second, ...) — добавление данных одного или нескольких результатов 
(гарантируется, что количество параметров будет чётным);
get_sum() — возвращает пару сумм результатов экспериментов;
get_average() — возвращает пару средних арифметических значений результатов экспериментов.
Все вычисления производятся с точностью до сотых.

Примечание
В решении не должно быть вызовов требуемых функций.

Ввод:
enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())

Вывод:
(9, 12) (3.0, 4.0)
(10, 14) (2.5, 3.5)
"""

# 1 вариант решения:
def enter_results(*args):
    result.extend(args)
    

def get_sum():
    global sum_odd
    sum_odd = 0
    global sum_even 
    sum_even = 0
    global count_odd 
    count_odd = 0
    global count_even 
    count_even = 0
    for i in range(len(result)):
        if i % 2 != 0:
            sum_odd += result[i]
            count_odd += 1
        else:
            sum_even += result[i]
            count_even += 1
    return (round(sum_even, 2), round(sum_odd, 2))


def get_average():
    return (round(sum_even / count_even, 2), round(sum_odd / count_odd, 2))


result = []


# 2 вариант решения:
def enter_results(*args):
    data.extend(args)


def get_sum():
    return (round(sum(data[::2]), 2), round(sum(data[1::2]), 2))


def get_average():
    return (round(sum(data[::2])/len(data[::2]), 2), round(sum(data[1::2])/len(data[1::2]), 2))


data = []