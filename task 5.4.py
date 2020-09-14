print('Задание №4')
numbers_dict = {"One": "Один",
                "Two": "Два",
                "Three": "Три",
                "Four": "Четыре",
                "Five": "Пять"}
try:
    with open('files/file4.txt') as file, open('files/file4_res.txt', 'w') as res_file:
        lines_from_file = [line.split() for line in file]
        new_lines = [[numbers_dict[el[0]], el[1], el[2]] for el in lines_from_file]
        for el in new_lines:
            res_file.writelines(' '.join(el) + '\n')
except IOError:
    print('Ошибка ввода/вывода')
