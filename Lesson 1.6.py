print('Задача 6. Проверяем бухгалтера')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print ((num1 % 100)+(num2 % 100))4