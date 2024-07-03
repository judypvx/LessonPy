# Задача 2. Таблица суммы
# Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 1 до N.
# Пример:


mumber_to_sum = int(input('Enter a number: '))

for row in range(mumber_to_sum + 1):
    for col in range(mumber_to_sum + 1):
        print(col + row, end='\t')
    print()