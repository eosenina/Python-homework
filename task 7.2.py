from abc import ABC, abstractmethod
print('Задание №2')


class Habiliment(ABC):
    """ Базовый класс предмет одежды """
    def __init__(self, value):
        self.__name = value

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Habiliment):
    """ Класс пальто """
    def __init__(self, size):
        super().__init__('пальто')
        self.__size = size

    def fabric_consumption(self):
        return self.__size / 6.5 + 0.5


class Costume(Habiliment):
    """ Класс костюм """
    def __init__(self, height):
        super().__init__('костюм')
        self.__height = height

    def fabric_consumption(self):
        return self.__height * 2 + 0.3


def print_consumption(hab):
    print(f'Расход ткани на {hab.name} равен {hab.fabric_consumption()}')


c = Coat(50)
d = Costume(150)
print_consumption(c)
print_consumption(d)
