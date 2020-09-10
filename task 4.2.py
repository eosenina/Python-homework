import random
print('Задание №2')
rand_ls = [random.randint(0, 1000) for i in range(20)]
print('Исходный список: ', rand_ls)
new_ls = [rand_ls[i] for i in range(1, len(rand_ls)) if rand_ls[i] > rand_ls[i-1]]
print('Полученный список: ', new_ls)

