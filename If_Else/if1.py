yesterday_temp = int(input()) # Температура вчера
today_temp = int(input()) # Температура сегодня
if today_temp > yesterday_temp: # if (если) = основное условие
    print("Сегодня теплее, чем вчера.")
elif today_temp < yesterday_temp: # elif (иначе если) = проверяется, если if ложное, может быть много, или 0
    print("Сегодня холоднее, чем вчера.")
else: # else (иначе) = выполняется только, если if и elif не выполнились, не имеет условия
    print("Сегодня такая же температура, как вчера.")