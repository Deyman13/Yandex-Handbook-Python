# Метод	str.join(str_col)
# Описание	Возвращает строку, полученную конкатенацией (сложением) строк — элементов коллекции str_col 
# (обозначение коллекции с элементами типа данных «строка»). Разделителем является строка, для которой вызван метод
a = ["1", "2", "3"]
print("; ".join(a))
a = ["katya", "lena", "borya"]
print(" | ".join(a))
# Результат	"1; 2; 3" , katya | lena | borya
