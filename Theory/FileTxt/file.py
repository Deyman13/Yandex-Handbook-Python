# 1 способ работы с файлом txt
colors = ["red", "green", "blue"]
data = open("file.txt", "a") 
data.writelines(colors)
data.close()

# 2 способ работы с файлом txt
with open("file.txt", "a") as data:
    data.write("\nLine1\n")
    data.write("Line2\n")
# автоматически закрывает файл после выполнения действий с ним.

# Есть 3 модификатора, a, w и r (a - дописать, w - переписать (удалить все старое, и заново написать), r - прочесть)
path = "file.txt"
data = open(path, "r")
for line in data:
    print(line)
data.close()





