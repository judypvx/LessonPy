# Задача 1. Матрица
# Напишите программу, которая выводит квадратную матрицу размера N на N.
# В каждой нечётной строке матрицы идут числа от 1 до N, а в каждой чётной — просто числа, равные номеру этой строки.
# Пример:


mumber = int(input('Enter a number: '))

for row in range(1, mumber + 1 ):

    for col in range(1, mumber + 1):
        if row %2 == 0:
            print(row, end=" ")
        else:
            print(col, end=" ")

    print()