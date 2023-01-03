import timeit
# 1. Оператор использование нотации среза (Является самым быстрым, и рекомендуемым способом реверсии)
def rev_string1(s): 
    return s[::-1] # начиная с -1, пройдите весь путь, делая шаги по -1

# 2. Использование функции reversed() (в 7.5 раз медленнее среза, но хороший способ)
def rev_string2(s): 
    return ''.join(reversed(s))

# 3. Использование рекурсии
def rev_string3(s): 
    if len(s) == 1:
        return s
    return s[-1] + rev_string3(s[:-1])

# 4. Классический способ (не рекомендуется, в 71 раз медленнее среза)
def rev_string4(s):
    chars = list(s)
    for i in range(len(s) // 2):
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp
    return ''.join(chars)

print(rev_string1("Hello, world"))
print(rev_string2("Hello, world"))
print(rev_string3("Hello, world"))
print(rev_string4("Hello, world"))







    




        



