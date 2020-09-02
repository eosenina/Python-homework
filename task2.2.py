print('Задание №2')
while True:
    ls = input("Введите элементы списка через пробел: ")
    ls = ls.split()
    print(ls)
    i = 0
    while i < len(ls) - 1:
        temp = ls[i]
        ls[i] = ls[i + 1]
        ls[i + 1] = temp
        i += 2
    print(f'Преобразованный список: {ls}')
    ans = input('Введите Y/y, чтобы попробовать ещё раз, любые другие символы для выхода: ')
    if ans == 'y' or ans == 'Y':
        continue
    else:
        break
