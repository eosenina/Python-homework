print('Задание №2')
while True:
    number = input('Введите время в секундах: ')
    if number.isdigit():
        number = int(number)
        time_h = number // 3600
        number = number % 3600
        time_min = number // 60
        time_sec = number % 60
        print("Заданное время {}:{:02}:{:02}".format(time_h, time_min, time_sec))
        time_d = time_h // 24
        time_h = time_h % 24
        if time_d > 0:
            print("или {} дней и {:02}:{:02}:{:02}".format(time_d, time_h, time_min, time_sec))
        else:
            print("или {:02}:{:02}:{:02}".format(time_h, time_min, time_sec))
        break
    else:
        print('Ошибка ввода')

