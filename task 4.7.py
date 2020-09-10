print('Задание №7')


def my_fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


while True:
    user_ans = input('Введите целое положительное число: ')
    if user_ans.isdigit():
        user_ans = int(user_ans)
        break
    else:
        print('Ошибка ввода! Попробуйте ещё раз.')

for el in my_fact(user_ans):
    print(el)

