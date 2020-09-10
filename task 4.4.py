import random
print('Задание №4')


def is_unique(num, num_list):
    """
    Функция проходит по списку и проверяет, является ли
    переданное в первом параметре значение уникальным элементом
    списка, переданного во втором параментре
    """
    count = 0
    for elem in num_list:
        if num == elem:
            count += 1
        if count > 1:
            return False
    return False if count == 0 else True


rand_ls = [random.randint(0, 20) for i in range(20)]
print('Исходный список: ', rand_ls)
new_ls = [el for el in rand_ls if is_unique(el, rand_ls)]
print('Полученный список: ', new_ls)
