# 1. Работа со структурами данных
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0])    # Вывод первого элемента
print(my_list[2])    # Вывод третьего элемента
print(my_list[-1])   # Вывод последнего элемента
my_list[1] = 100     # Замена второго элемента

# 2. Работа с циклами
for i in range(1, 11):
    print(i)

i = 10
while i >= 1:
    print(i)
    i -= 1


    
# 3. Работа с условными операторами
num = int(input("Введите число: "))
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")
num = int(input("Введите число: "))
if num > 0:
    print("Число положительное")
elif num < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# 4. Домашнее задание
# №1
a = int(input())
for i in range(1, a+1):
    print(i)
# №2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a>b:
    print("Большее: ", a)
elif a<b:
    print("Большее: ", b)
else:
    print("Большее: ", a)





    
