print('Задание №1')

try:
    with open('files/file1.txt', 'w') as file:
        while True:
            user_ans = input('Введите строку для записи в файл: ')
            if user_ans == '':
                break
            file.write(user_ans + '\n')
except IOError:
    print('Ошибка ввода/вывода')


