print('Задание №3')


def my_func(num1, num2, num3):
    u_args = (num1, num2, num3)
    return sum(u_args) - min(u_args)


def input_integer(invitation_text):
    while True:
        i_num = input(invitation_text)
        try:
            i_num = int(i_num)
            return i_num
        except ValueError:
            print('Ошибка ввода! Попробуйте ещё раз.')


n1 = input_integer('Введите первое число: ')
n2 = input_integer('Введите второе число: ')
n3 = input_integer('Введите третье число: ')
print(f'Сумма двух наибольших чисел = {my_func(n1, n2, n3)}')

