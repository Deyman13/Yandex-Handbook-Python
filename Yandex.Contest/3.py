# В первой строке входных данных записан номер телефона, который Вася хочет добавить в адресную книгу своего телефона. 
# В следующих трех строках записаны три номера телефонов, которые уже находятся в адресной книге телефона Васи. 
# Гарантируется, что каждая из записей соответствует одному из трех приведенных в условии форматов.
# Если код не указан, то считается, что он равен 495.

# Формат вывода
# Для каждого телефонного номера в адресной книге выведите YES (заглавными буквами), если он совпадает 
# с тем телефонным номером, который Вася хочет добавить в адресную книгу или NO (заглавными буквами) в противном случае.

def sort(s):
    temp = []
    for i in range(len(s)):
        if s[i] != "(" and s[i] != ")" and s[i] != "-" and s[i] != "+":
            temp.append(s[i])
    if len(temp) <= 7:
        temp.insert(0, "4")
        temp.insert(1, "9")
        temp.insert(2, "5")
    if len(temp) > 10:
        del temp[0]
    return temp
def isthisnumbertrue(x, num):
    if x == num:
        return print("YES")
    return print("NO")
num = list(sort(input()))
f = list(sort(input()))
s = list(sort(input()))
t = list(sort(input()))
isthisnumbertrue(f,num)
isthisnumbertrue(s,num)
isthisnumbertrue(t,num)



