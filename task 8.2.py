print('Задание №2')


class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


d = input('Введите делитель: ')
try:
    d = int(d)
    if d == 0:
        raise MyZeroDivision('Деление на ноль!')
    res = 100 / d
except ValueError:
    print('Ошибка ввода!')
except MyZeroDivision as error:
    print(error.txt)
else:
    print(f'Результат 100/{d} = {res}')
