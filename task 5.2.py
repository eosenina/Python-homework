print('Задание №2')

try:
    with open('files/file2.txt') as file:
        file_lines = []
        for i, line in enumerate(file):
            line = str.rstrip(line, '\n')
            file_lines.append(line)
            print(f'В {i + 1} строке {len(line)} символов')
            print(line)
        print('Количество строк в файле:', len(file_lines))

except IOError:
    print('Ошибка ввода/вывода')
