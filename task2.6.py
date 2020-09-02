print('Задание №6')
goods = [(1, {'название': 'колбаса', 'цена': 22, 'количество': 2, 'единица измерения': 'шт'}),
         (444, {'название': 'сыр', 'цена': 66, 'количество': 38, 'единица измерения': 'кг'}),
         (4, {'название': 'молоко', 'цена': 23, 'количество': 4, 'единица измерения': 'л'})
         ]
index_dict = {1: 0, 444: 1, 4: 2}
goods_stat = {}


def index_update(ind_dict, del_num):
    val = ind_dict.pop(del_num)
    for key in ind_dict.keys():
        if ind_dict[key] > val:
            ind_dict[key] -= 1


while True:
    ans = input('Введите n - для добавления нового товара, d - для удаления товара, '
                'l - для вывода списка товаров, s - для вывода статистики, q - для выхода: ')
    if ans == 'q':
        break
    elif ans == 'l':
        for gd in goods:
            print(gd)
        continue
    elif ans == 'n':
        success = False
        while not success:
            good_id = input('Введите номер товара (целое неотрицательное число): ')
            if good_id.isdigit():
                good_id = int(good_id)
                if good_id in index_dict:
                    ans = input('Товар с таким номером уже есть. Перезаписать его - r, '
                                'ввести другой номер - любая клавиша.')
                    if ans == 'r':
                        success = True
                    else:
                        continue
                else:
                    success = True
            else:
                print('Ошибка ввода! Попробуйте ещё раз.')

        name = input('Введите название товара: ')
        success = False
        while not success:
            price = input('Введите цену товара (целое неотрицательное число): ')
            if price.isdigit():
                price = int(price)
                success = True
            else:
                print('Ошибка ввода! Попробуйте ещё раз.')

        success = False
        while not success:
            count = input('Введите количество товара (целое неотрицательное число): ')
            if count.isdigit():
                count = int(count)
                success = True
            else:
                print('Ошибка ввода! Попробуйте ещё раз.')

        measure = input('Введите единицу измерения: ')

        good_info = {'название': name, 'цена': price, 'количество': count, 'единица измерения': measure}

        if good_id in index_dict:
            i = index_dict.get(good_id)
            goods[i][1].update(good_info)
        else:
            goods.append((good_id, good_info))
            index_dict.update({good_id: len(goods) - 1})

    elif ans == 's':
        goods_stat.clear()
        for gd in goods:
            for k in gd[1].keys():
                if k in goods_stat:
                    if not gd[1][k] in goods_stat[k]:
                        goods_stat[k].append(gd[1][k])
                else:
                    goods_stat.update({k: [gd[1].get(k)]})
        for item in goods_stat.items():
            print(item)

    elif ans == 'd':
        while True:
            num = input('Введите номер товара, который необходимо удалить: ')
            if num.isdigit():
                num = int(num)
                if num in index_dict:
                    goods.pop(index_dict[num])
                    index_update(index_dict, num)
                else:
                    print('Товара с таким номером нет.')
                break
            else:
                print('Ошибка ввода! Попробуйте ещё раз!')
