print('Задание №3')


class IsListOfNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt


lst_of_num = []
while True:
    user_ans = input('Введите число или "q" - для окончания ввода: ')
    if user_ans == 'q':
        break
    try:
        if not user_ans.isdigit():
            raise IsListOfNumbers('Введено не число!')
        lst_of_num.append(int(user_ans))
    except IsListOfNumbers as error:
        print(error.txt)

print(lst_of_num)
