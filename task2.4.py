print('Задание №4')
while True:
    user_str = input('Введите строку: ')
    words_list = user_str.split()
    i = 0
    for word in words_list:
        print(f'{i}: {word[0:10]}')
        i += 1

    ans = input('Введите Y/y, чтобы попробовать ещё раз, любые другие символы для выхода: ')
    if ans == 'y' or ans == 'Y':
        continue
    else:
        break
