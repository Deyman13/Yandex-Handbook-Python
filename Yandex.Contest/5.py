t = list(map(int, input().split(" "))) 
x = t[3]
x2 = t[4]
x3 = 0
number_of_apartments = t[2] / t[4] # узнаем сколько квартир может находиться на одном этаже 
number_of_apartments_per_floor = round(number_of_apartments) * t[1] # узнаем максимум квартир в подъезде (80)
if all(t) > 0 and all(t) < 10 ** 6 and t[2] >= t[4]: # если все названные переменные больше 0 и меньше 10^6
    if t[3] >= 1: # если подъезд больше 1 
        while t[3] > 1:
            x3 += number_of_apartments_per_floor * t[3]
            t[3] -= 1
        if t[2] > x3 / x:
            if t[0] > number_of_apartments_per_floor: # если номер квартиры больше, чем макс кол-во квартир в подъезде
                while t[0] > number_of_apartments_per_floor: # до тех пор, пока номер больше, чем макс кол-во
                    t[0] -= number_of_apartments_per_floor # вычитаем макс кол-во квартир из нашего номера
                    t[3] += 1 # и с каждой итерацией добавляем единичку, как переход на новый подъезд
                if t[3] > x + 1: # если текущий подъезд больше, чем указанный ко второй квартире + 1
                    t[3] = 0 # обнуляем подъезд, делая его неизвестным
            floor = t[0] / number_of_apartments # узнаем этаж деля остаток номера квартиры на кол-во квартир на этаже
            if floor <= t[1]: # если этаж меньше, чем максимальный
                if floor > t[0] // number_of_apartments: # если деление больше чем целочисленное деление
                    floor += 1 # то добавляем этаж
                if floor > x2 + 1:
                    floor = 0
                if t[3] == 0 and floor == 0:
                    print(-1, -1)
                else:
                    print(t[3], int(floor))
            else:
                print(-1, -1)
        else:
            print(-1, -1)
    else:
        print(-1, -1)
else:
    print(-1, -1)









