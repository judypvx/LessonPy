#Задача 3. Факториал
#Что нужно сделать
#Мы всё ближе и ближе подбираемся к серьёзной математике. Одна из классических задач — задача на нахождение факториала числа. И в будущем мы с ней ещё встретимся.
#Дано натуральное число n. Напишите программу, которая находит n! (n-факториал).
#Запись n! означает следующее:
#n! = 1 * 2 * 3 * 4 * 5 * … * n
#Пример:
#Введите число: 5
#Факториал числа 5 равен 120


factorial = 1
n = int(input("Enter a number: "))
for count in range(1,n+1):
     factorial = factorial*count
print(factorial)


