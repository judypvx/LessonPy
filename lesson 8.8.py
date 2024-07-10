seqNum = int(input("Сколько будет чисел: "))
numeral = int(input("Как цифру считать: "))
while numeral < 0 or numeral > 9:
    numeral = int(input("Цифра должна быть от 0 до 9, Введите новую: "))
numeralCount = 0
for num in range(seqNum):
    print("введите", num, 'число', end="")
    number = int(input())
    while number > 0:
        if number % 10 == numeral:
            numeralCount += 1
        number //= 10
print("Цифр", numeral, 'в последовательности', numeralCount)