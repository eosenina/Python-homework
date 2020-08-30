print('Задание №5')
proceeds = float(input('Введите сумму выручки: '))
expenses = float(input('Введите сумму издержек: '))
if proceeds > expenses:
    rent = proceeds / expenses
    print(f'Фирма отработала с прибылью. Рентабельность выручки {rent}.')
    count = int(input('Введите количество сотрудников фирмы: '))
    profit = (proceeds - expenses) / count
    print(f'Чистая прибыль в рассчете на 1 сотрудника составляет {profit}')
elif proceeds < expenses:
    print('Фирма отработала в убыток.')
else:
    print('Прибыль и расходы равны')


