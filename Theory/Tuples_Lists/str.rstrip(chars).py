# Метод	str.rstrip(chars)
# Описание	Возвращает строку, у которой в конце удалены символы, встречающиеся в строке chars. 
# Если значение chars не задано, то пробельные символы удаляются
s = "stringBCCADDDABC"
print(s.rstrip("ABCD"))
s = "stringB.C.D.A"
print(s.rstrip("ABCD"))
s = "stringB.C.D.A"
print(s.rstrip(".ABCD"))
# Результат	"string", "stringB.C.D.", "string"
