from functools import reduce
import random
print('Задания №4-6')


class Storage:
    """ Класс склад """
    def __init__(self):
        self.__equipment = {}  # словарь хранящейся на складе оргтехники
        self.__transferred = []  # список переданной оргтехники

    @property
    def equipment(self):
        return self.__equipment

    @property
    def transferred_equipment(self):
        return self.__transferred

    def __str__(self):
        res = ''
        for key, val in self.__equipment.items():
            res = res + str(key) + ' ' + str(val[0].name) + ' '\
                  + str(val[0].model) + ' ' + str(val[1]) + 'шт\n'
        return res

    def get_transferred_str(self):
        res = ''
        for val in self.__transferred:
            res = res + str(val[0]) + ' ' + str(val[1].name) + ' ' + str(val[1].model) \
                  + ' ' + str(val[2]) + 'шт ' + str(val[3]) + '\n'
        return res

    def __code_exists(self, code):
        if code in self.__equipment.keys():
            return True
        return False

    def __gen_new_code(self):
        while True:
            new_code = random.randint(10000, 99999)
            if not self.__code_exists(new_code):
                return new_code

    def add_equipment(self, obj, quantity, code=0):
        """
        Добавление оргтехники на склад
        :param obj: OfficeEquipment
        :param quantity: количество
        :param code: артикул (по умолчанию генерируется)
        :return:
        """
        if not isinstance(obj, OfficeEquipment):
            raise Exception('Переданный объект невозможно добавить на склад')
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError('Недопустимое значение количества единиц техники')
        if code == 0:
            code = self.__gen_new_code()
        elif self.__code_exists(code):
            raise Exception('Введенный артикул уже существует')

        self.__equipment.update({code: [obj, quantity]})

    def del_equipment(self, code):
        """ Удаление со склада по артикулу """
        if not self.__code_exists(code):
            raise Exception('Такого артикула на складе нет')
        self.__equipment.pop(code)

    def transfer_equipment(self, code, destination, quantity):
        """
        Передача техники со склада
        :param code: артикул оргтехники
        :param destination: куда передано
        :param quantity: количество
        """
        if not self.__code_exists(code):
            raise Exception('Такого артикула на складе нет')
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError('Недопустимое значение количества единиц техники')
        if self.__equipment[code][1] < quantity:
            raise Exception('На складе нет указанного количества')
        eq = self.__equipment[code][0]
        self.__transferred.append([code, eq, quantity, destination])
        if self.__equipment[code][1] == quantity:
            self.del_equipment(code)
        else:
            self.__equipment[code][1] -= quantity

    def calculate_volume(self):
        return reduce(lambda eq1, eq2: eq1 + eq2, [eq[1] * eq[0].vol for eq in self.__equipment.values()])

    def add_unit(self, code, quantity):
        if not self.__code_exists(code):
            raise Exception('Нет записи с таким артикулом')
        if not isinstance(quantity, int):
            raise ValueError('Недопустимый тип аргумента')

        self.__equipment[code][1] += quantity


class OfficeEquipment:
    """ Класс оргтехника """
    def __init__(self, name, model, vol):
        if not isinstance(vol, (float, int)) or vol <= 0:
            raise ValueError('Недопустимое значение занимаемого объема одной единицы техники')

        self.__name = name
        self.__model = model
        self.__volume = vol

    @property
    def name(self):
        return self.__name

    @property
    def model(self):
        return self.__model

    @property
    def vol(self):
        return self.__volume


class Printer(OfficeEquipment):
    """ Класс принтер """
    def __init__(self, model, vol, print_speed, cartridge):
        if not isinstance(print_speed, int) or print_speed <= 0:
            raise ValueError('Недопустимое значение количества единиц техники')
        super().__init__('Принтер', model, vol)
        self.__print_speed = print_speed
        self.__cartridge = cartridge

    @property
    def print_speed(self):
        return self.__print_speed

    @property
    def cartridge(self):
        return self.__cartridge


class Scanner(OfficeEquipment):
    """ Класс сканер """
    def __init__(self, model, vol, resolution):
        super().__init__('Сканер', model, vol)
        self.__resolution = resolution

    @property
    def resolution(self):
        return self.__resolution


s = Storage()
pr = Printer('Epson C45', 50, 100, 'A155')
pr2 = Printer('Canon qw322', 66.2, 60, 'x122')
sc = Scanner('HP', 20, '600x1200')
s.add_equipment(pr, 10, 778)
s.add_equipment(pr2, 2)
s.add_equipment(sc, 7)
print(s)
s.transfer_equipment(778, 'hr', 5)
s.add_unit(778, 1)
print(s)
s.transfer_equipment(778, 'office', 5)
print('Склад:\n', s)
print('Передано:\n', s.get_transferred_str())
