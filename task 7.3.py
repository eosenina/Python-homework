print('Задание №3')


class Cell:
    """ Класс клетка """
    def __init__(self, alveolus):
        if type(alveolus) is not int:
            raise ValueError
        if alveolus <= 0:
            raise ValueError('Количество ячеек в клетке должно быть больше 0')
        self.alveolus_count = alveolus

    def __add__(self, other):
        if type(other) is not Cell:
            raise ValueError
        return Cell(self.alveolus_count + other.alveolus_count)

    def __mul__(self, other):
        if type(other) is not Cell:
            raise ValueError
        return Cell(self.alveolus_count * other.alveolus_count)

    def __truediv__(self, other):
        if type(other) is not Cell:
            raise ValueError
        new_al_count = self.alveolus_count // other.alveolus_count
        if new_al_count == 0:
            raise ValueError('В результате деления ячеек не осталось')
        return Cell(new_al_count)

    def __sub__(self, other):
        if type(other) is not Cell:
            raise ValueError
        new_al_count = self.alveolus_count - other.alveolus_count
        if new_al_count <= 0:
            raise ValueError('После вычитания ячеек не осталось')
        return Cell(new_al_count)

    def make_order(self, row):
        num = self.alveolus_count
        result = ''
        while num > row:
            result = result + '*' * row + '\n'
            num -= row
        result = result + '*' * num
        return result


c = Cell(20)
print(c.make_order(30))
d = Cell(70)
print(d.make_order(4))
k = Cell(11)
a = d - c + k
print(a.make_order(5))
print(a.alveolus_count)
a = d * c
print(a.alveolus_count)
a = a / k
print(a.alveolus_count)

