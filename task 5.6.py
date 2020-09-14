print('Задание №6')

try:
    with open('files/file6.txt') as file:
        courses_dict = {}
        for line in file:
            hours = line.split()
            for i in range(1, 4):
                if hours[i] != '-':
                    hours[i] = int(hours[i].rstrip('(лпраб)'))
                else:
                    hours[i] = 0
            courses_dict[hours[0].rstrip(':')] = sum(hours[1:])
        print(courses_dict)
except IOError:
    print('Ошибка ввода/вывода')
except ValueError:
    print('Неверные входные данные')
