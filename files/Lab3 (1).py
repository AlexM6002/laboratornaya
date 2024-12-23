#Чтение всего файла
with open('example.txt', 'r') as file:
    content = file.read()
#Построчное чтение
with open('example.txt', 'r') as file:
    for line in file:
        print(line)

a = input("F or S: ")
if a==F:
    with open('example.txt', 'r') as file:
        content = file.read()
else:
    with open('example.txt', 'r') as file:
        for line in file:
            print(line)


# 2

with open('example.txt', 'w') as file:
    file.write("hello world")

with open('example.txt', 'a') as file:
    file.write("\nHello world")

# 3
try:
    with open('example.txt', 'r') as file:
        content = file.read()
except:
    FileNotFoundError
    
    
