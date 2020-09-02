print('Задание №1')


def convert_element(type_char):
    global elem
    if type_char == 'i':
        try:
            elem = int(elem)
            return True
        except ValueError:
            return False
    elif type_char == 'f':
        try:
            elem = float(elem)
            return True
        except ValueError:
            return False
    elif type_char == 'b':
        if elem in {'True', 'true', 'TRUE', 't', 'T', '1'}:
            elem = True
            return True
        elif elem in {'False', 'false', 'FALSE', 'F', 'f', '0'}:
            elem = False
            return True
        else:
            return False
    elif type_char == 's':
        return True
    elif type_char == 'l':
        elem = elem.split()
        return True


arr = [3, 5, 3, 'Привет', 6.5, True, [1, 2, 3]]
print(f'Заданный список: {arr}')
for elem in arr:
    print(f'Элемент {elem} имеет тип {type(elem)}')

while True:
    ans = input('Создать новый список? y/n: ')
    if ans == 'y':
        types = {'i', 'f', 'b', 's', 'l'}
        new_arr = list()
        print('Введите значения и типы элементов нового списка или '
              'оставьте строку значения элемента пустой для окончания ввода.)')
        print('Типы элементов: i - целое число, f - вещественное число, b - логический тип, s - строка, l - список.')
        print('Для ввода логической переменной допускаются значения: True, False, true, false, TRUE, FALSE, 0, 1 ')
        print('При вводе списка разделителем между элементами является пробел')
        elem = input('Значение: ')
        while elem != '':
            type_char = input('Тип: ')
            if not (type_char in types):
                print('Ошибка! Попробуйте ещё раз.')
                continue
            if convert_element(type_char):
                new_arr.append(elem)
            else:
                print('Ошибка! Попробуйте ещё раз.')
            elem = input('Значение: ')
        print(f"Ваш список: {new_arr}")
        for elem in new_arr:
            print(f'Элемент {elem} имеет тип {type(elem)}')
    elif ans == 'n':
        break
    else:
        print('Ошибка! Попробуйте ещё раз.')
        continue
