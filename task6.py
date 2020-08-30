print('Задание №6')
first_dist = float(input('Введите дистанцию, пройденную в первый день: '))
goal_dist = float(input('Введите цель: '))
new_dist = first_dist
day_count = 1
while new_dist < goal_dist:
    new_dist = new_dist * 1.1
    day_count += 1
    print("{} день - {:.3f}".format(day_count, new_dist))
print(f'Цель будет достигнута на {day_count} день')