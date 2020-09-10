import sys
from itertools import count, cycle
print('Задание №6')

my_str = 'I will not obey the voices in my head'
my_lst = my_str.split()
end_line = 'head'
try:
    st_point = int(sys.argv[1])
except ValueError:
    print('Переданный параметр - не число')
except IndexError:
    print('Не был введен параметр')

for num in count(st_point):
    if num > 100:
        break
    print(num)
line_count = 0
for word in cycle(my_lst):
    print(word, end=' ')
    if word == end_line:
        line_count += 1
        print("")
    if line_count == st_point:
        break


