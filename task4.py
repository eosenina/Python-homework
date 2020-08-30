print('Задание №4')
while True:
    number = input('Введите целое положительное число: ')
    if number.isdigit():
        number = int(number)
        max_num = 0
        while number > 0:
            last = number % 10
            if last > max_num:
                max_num = last
            number = number // 10
        print(f'Максимальная цифра в записи числа - {max_num}')
        break
    else:
        print('Ошибка ввода')

