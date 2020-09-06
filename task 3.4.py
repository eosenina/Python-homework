print('Задание №4')


def my_pow(a, exp):
    """
    Функция реализует бинарный алгоритм возведения числа в степень.
    :param a: основание степени
    :param exp: показатель степени
    :return: результат возведения числа а в степень exp
    """
    res = 1
    n = abs(exp)
    while n:
        if n % 2 == 0:
            a *= a
            n = n >> 1
        else:
            n -= 1
            res *= a
    return 1 / res if exp < 0 else res


def input_neg_integer(invitation_text):
    while True:
        i_num = input(invitation_text)
        try:
            i_num = int(i_num)
            if i_num >= 0:
                print('Ошибка ввода! Попробуйте ещё раз.')
            else:
                return i_num
        except ValueError:
            print('Ошибка ввода! Попробуйте ещё раз.')


def input_pos_float(invitation_text):
    while True:
        f_num = input(invitation_text)
        try:
            f_num = float(f_num)
            if f_num <= 0:
                print('Ошибка ввода! Попробуйте ещё раз.')
            else:
                return f_num
        except ValueError:
            print('Ошибка ввода! Попробуйте ещё раз.')


num = input_pos_float('Введите действительное положительное число: ')
b = input_neg_integer('Введите целый отрицательный показатель степени: ')

print('Результат: ', my_pow(num, b))
