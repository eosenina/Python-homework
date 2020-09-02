print('Задание №3')
seasons_list = [['зима', {12, 1, 2}],
                ['весна', {3, 4, 5}],
                ['лето', {6, 7, 8}],
                ['осень', {9, 10, 11}]]
seasons_dict = {1: 'зима',
                2: 'зима',
                3: 'весна',
                4: 'весна',
                5: 'весна',
                6: 'лето',
                7: 'лето',
                8: 'лето',
                9: 'осень',
                10: 'осень',
                11: 'осень',
                12: 'зима'
}
while True:
    ans = input('Введите месяц в виде числа от 1 до 12: ')
    if ans.isdigit():
        ans = int(ans)
        if ans < 1 or ans > 12:
            print('Ошибка ввода! Попробуйте ещё раз')
            continue
        else:
            # Решение с помощью list
            for season in seasons_list:
                if ans in season[1]:
                    print(f'list: {season[0]}')
                    break
            # Решение с помощью dict
            if ans in seasons_dict:
                print(f'dict: {seasons_dict.get(ans)}')
    else:
        print('Ошибка ввода! Попробуйте ещё раз')
        continue

    ans = input('Введите Y/y, чтобы попробовать ещё раз, любые другие символы для выхода: ')
    if ans == 'y' or ans == 'Y':
        continue
    else:
        break
