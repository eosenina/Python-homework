print('Задание №3')
while True:
    a = input('Введите число от 0 до 9: ')
    if a.isdigit():
        a = int(a)
        if a > 0 and a < 10:
            result = a * 100 + a * 20 + a * 3
            print(f"n + nn + nnn = {result}")
            break
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')
