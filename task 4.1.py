import sys
print('Задание №1')

user_arg = sys.argv

try:
    result = float(user_arg[1]) * float(user_arg[2]) + float(user_arg[3])
except ValueError:
    print('Не удалось преобразовать аргументы в числа')
except IndexError:
    print('Неверное количество аргументов!')
else:
    print(f'Зарплата = {result}')

