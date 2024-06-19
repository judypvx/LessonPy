print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно



number1 = int(input("Введите число 1:"))
number2 = int(input("Введите число 2:"))
number3 = int(input("Введите число 3:"))


if number1 > number2 and number1 > number3:
    print (number1)
elif number2 > number1 and number2 > number3:
    print (number2)
elif number3 > number1 and number3 > number2:
    print (number3)

