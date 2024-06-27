#Задача 5. Отрезок
#Что нужно сделать
#Напишите программу, которая считывает с клавиатуры два числа: a и b, — считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.



a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

total = 0
counter = 0

for count in range(a, b+1):
    if count % 3 == 0:

        total += count
        counter += 1

print(total/counter)
