# Задача 4. Среднее на отрезке
# Что нужно сделать
# Напишите программу, которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.
# Рекомендации
# Функция range(start, stop) не включает границу stop, останавливается, не доходя до неё.



a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))
c = int(input("Enter a number C: "))

count_medium = 0
count_number = 0


for number in range (a,b+1):
    if number % c == 0:
        count_number += 1
        count_medium += number

print(count_medium/count_number)


