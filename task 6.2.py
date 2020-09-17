print('Задание №2')


class Road:
    __ASPHALT_PER_M = 20
    __THICKNESS = 5
    _length = 0
    _width = 0

    def __init__(self, length, width):
        if not type(length) is int or not type(width) is int:
            raise Exception('Неверные параметры конструктора')
        if length < 0 or width < 0:
            raise Exception('Неверные параметры конструктора')
        self._length = length
        self._width = width

    def asphalt_count(self):
        return self._width * self._length * Road.__ASPHALT_PER_M * Road.__THICKNESS


a = Road(11, 12)
print(a.asphalt_count())
