import random
print('Задание №5')


def find_index(rates, new_val):
    left = 0
    right = len(rates) - 1
    while left <= right:
        i = (right + left) // 2
        if rates[i] >= new_val:
            left = i + 1
        else:
            right = i - 1
    return left


def fill_and_check(rates):
    i = 0
    while i < 30:
        new_val = random.randint(1, 100)
        pos = find_index(rates, new_val)
        rates.insert(pos, new_val)
        i += 1
        print(pos, new_val)
        print(rates)
    i = 0
    while i < len(rates)-1:
        if rates[i] < rates[i + 1]:
            print('Wrong!')
            break
        i += 1


rate_list = [50, 20, 20]
print('Текущий рейтинг: ', rate_list)
while True:
    new_rate = input('Введите новое значение (натуральное число), q для выхода или f для автоматического заполнения: ')
    if new_rate == 'q':
        break
    if new_rate == 'f':
        fill_and_check(rate_list)
        break
    if new_rate.isdigit():
        new_rate = int(new_rate)
        if new_rate <= 0:
            print('Ошибка ввода! Попробуйте ещё раз.')
            continue
        pos = find_index(rate_list, new_rate)
        rate_list.insert(pos, new_rate)
        print('Текущий рейтинг: ', rate_list)
    else:
        print('Ошибка ввода! Попробуйте ещё раз.')
        continue
