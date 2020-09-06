print('Задание №5')
exit_char = 'q'


def check_list(user_list):
    """
    Функция приводит введенные пользователем данные к типу int,
    и отслеживает, содержит ли последовательность символ окончания работы.
    :param user_list: список слов
    :return:'t' - все элементы успешно приведены к типу int;
    'f' - элементы списка не удалось привести к типу int;
    либо индекс элемента списка, содержащего символ окончания работы
    """
    for i in range(0, len(user_list)):
        try:
            user_list[i] = int(user_list[i])
        except ValueError:
            if exit_char in user_list[i]:
                return i
            else:
                return 'f'
    return 't'


user_input = ''
print(f'Вводите числа через пробел. Для выхода введите {exit_char}')
result = 0
while True:
    user_input = input()
    user_input = user_input.split()
    func_answer = check_list(user_input)
    if func_answer == 't':
        result += sum(user_input)
        print(result)
    elif func_answer == 'f':
        print('Ошибка ввода! Попробуйте ещё раз.')
        continue
    else:
        result += sum(user_input[:func_answer:])
        print(result)
        break
