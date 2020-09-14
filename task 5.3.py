print('Задание №3')

try:
    with open('files/file3.txt') as file:
        salary_sum = 0
        count = 0
        for line in file:
            name, sal = line.split()
            sal = int(sal)
            salary_sum += sal
            count += 1
            if sal < 20000:
                print(name, sal)
        print('Средняя зарплата: ', salary_sum / count)
except IOError:
    print('Ошибка ввода/вывода')
except ValueError:
    print('Неверные входные данные')
