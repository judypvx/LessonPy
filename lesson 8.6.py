# Задача 3. Координатные оси
# Напишите программу, которая рисует координатные оси на поле 20×50. Результат должен получиться таким:

x = 16
y = 50

for row in range(1, x + 1):
    for column in range(1, y + 1):

        if column == 25 and row == 8:
            print("╬",end="")
        elif column == 25:
            print("║", end="")
        elif row == 8:
            print("═", end="")
        else:
            print(" ", end="")


    print()

