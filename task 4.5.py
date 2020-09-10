from functools import reduce
print('Задание №5')
even_list = [i for i in range(100, 1001, 2)]
print('Произведение четных чисел от 100 до 1000 равно:\n', reduce(lambda a, b: a * b, even_list))
