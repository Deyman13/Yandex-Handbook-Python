# Метод	str.strip(chars)
# Описание	Возвращает строку, у которой в начале и в конце удалены символы, встречающиеся в строке chars. 
# Если значение chars не задано, то пробельные символы удаляются
s = "abcHello, world! cba"
print(s.strip(" abc"))
# Результат	"Hello, world!"