#
# Задача 2. Чёрный ящик
# Преподаватель показал студентам несколько результатов программы и сказал:
# «Кто догадается, что делает программа и как она это делает, получит зачёт автоматом».
# Студент Миша намерен получить этот зачёт.
# Он заметил, что в результатах программы есть определённая закономерность.

# https://prnt.sc/ZQ_jTWJxdSqe


number = int(input('Enter a number: '))

for row in range(1,number+1):
    for col in range(1,number+1):

        if col % 3 == 0:
            print (col,end=' ')
        else:
            print(row, end=' ')

    print()