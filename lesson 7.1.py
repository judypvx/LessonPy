'''
Задача 1. Урок литературы
Выполните задание, разобранное в уроке.
К уроку литературы нужно было прочитать “Евгения Онегина”. Учитель задаёт вопрос пяти случайным детям.
Она задаёт вопрос “Кто написал произведение?” и если ученик не угадывает, то учитель ставит двойку и спрашивает следующего.
Если хоть кто-то угадает, то вопросы больше не задаются. Напишите программу, которая посчитает количество двоечников из этих пяти.
'''

author_name = "Miyadzaki"

for author in range(1, 6):
    answer = input("Кто написал произведение?: ")
    if answer == author_name:
        break
    else:
        print("Садись, два!")