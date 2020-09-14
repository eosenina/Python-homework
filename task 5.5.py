import random
print('Задание №5')
try:
    with open('files/file5.txt', 'w+') as file:
        i = 0
        while i < 100:
            i += 1
            new_num = random.randint(0, 1000)
            file.write(str(new_num) + ' ')
        file.seek(0)
        f_content = [int(el) for el in file.read().split()]
        print('Сумма 100 случайных чисел: ', sum(f_content))

except IOError:
    print('Ошибка ввода/вывода')
