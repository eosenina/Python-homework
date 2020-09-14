import json
print('Задание №7')

try:
    with open('files/file7.txt') as file, open('files/file7_res.json', 'w') as file_res:
        firm_dict = {}
        count = 0
        average_profit = 0
        for line in file:
            firm_list = line.split()
            profit = int(firm_list[2]) - int(firm_list[3])
            firm_dict[firm_list[0]] = profit
            if profit > 0:
                average_profit += profit
                count += 1
        average_profit /= count
        result_list = [firm_dict, {'average_profit': average_profit}]
        print(result_list)
        json.dump(result_list, file_res)
except IOError:
    print('Ошибка ввода/вывода')
except ValueError:
    print('Неверные входные данные')
