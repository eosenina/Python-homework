print('Задание №1')


def funk_division(dividend, divider):
    if divider == 0:
        return None
    else:
        return dividend / divider


def input_float_number(invitation_text):
    while True:
        result = input(invitation_text)
        try:
            result = float(result)
            return result
        except ValueError:
            print('Ошибка ввода! Попробуйте ещё раз.')


a = input_float_number('Введите делимое: ')
b = input_float_number('Введите делитель: ')
res = funk_division(a, b)

if res is None:
    print('Деление на ноль!')
else:
    print(f'Результат деления: {res}')
