print('Задача 7. Почта')

# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед,
# а в 10:00 и 18:00 приезжают машины с посылками,
# и тогда все сотрудники на два часа заняты их разгрузкой.
# Во время обеда, разумеется, посылки никто не выдаёт,
# как и в моменты, когда разгружаются машины.

# Напишите программу,
# которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.

# Решите задание двумя способами:

# первый — при выполнении условия выводится сообщение:
# «Можно получить посылку»,

# второй —  при выполнении условия выводится сообщение:
# «Посылку получить нельзя».

time = int(input("Введите часы посещения почты: "))
if 8 <= time < 22 and not (14 <= time < 15 or 10 <= time < 12 or 18 <= time < 20):
    print("Посылку получить нельзя")
else:
    print("Можно получить посылку")



time = int(input("Введите часы посещения почты: "))
if not (8 <= time < 22 and not (14 <= time < 15 or 10 <= time < 12 or 18 <= time < 20)):
     print("Можно получить посылку")
else:
    print("Посылку получить нельзя")