print('Задание №7')


class ComplexNumber:
    """ Класс комплексное число """
    def __init__(self, x, y):
        """
        Создание комплексного числа
        :param x: действительная часть
        :param y: мнимая часть
        """
        if not (isinstance(x, (float, int)) and (isinstance(y, (float, int)))):
            raise ValueError('Недопустимый тип аргументов')
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __add__(self, other):
        """ Сложение двух комплексных чисел или комплексного числа с действительным """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.x + other.x, self.y + other.y)
        if isinstance(other, (float, int)):
            return ComplexNumber(self.x + other, self.y)
        raise ValueError('Недопустимый тип аргумента')

    def __mul__(self, other):
        """ Произведение двух комплексных чисел или произведение комплексного числа и действительного """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)
        if isinstance(other, (float, int)):
            return ComplexNumber(self.x * other,  self.y * other)
        raise ValueError('Недопустимый тип аргумента')

    def __str__(self):
        return str(self.x) + ' + ' + str(self.y) + 'i'


a = ComplexNumber(3, 4)
print(a)
b = ComplexNumber(4, 5)
print(b)
c = a + b
print(c)
c = a * b
print(c)
c = a + 3
print(c)
c = b * 5
print(c)
