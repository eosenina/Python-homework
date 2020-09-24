import datetime
print('Задание №1')


class Date:
    def __init__(self, day, month, year):
        if self.is_valid_date_num(day, month, year):
            self.__day = day
            self. __month = month
            self.__year = year
        else:
            raise ValueError('Недопустимые значения для даты')

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    def __str__(self):
        return f'{self.day:02}.{self.month:02}.{self.year}'

    __day_count_dict = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    @staticmethod
    def is_leap_year(year_int):
        """ Проверка, является ли год високосным """
        if not isinstance(year_int, int):
            raise ValueError
        if not (datetime.MINYEAR <= year_int <= datetime.MAXYEAR):
            raise ValueError('Недопустимое значение года')
        if year_int % 4 != 0 or (year_int % 100 == 0 and year_int % 400 != 0):
            return False
        return True

    @staticmethod
    def is_valid_date_num(day, month, year):
        if not (isinstance(day, int) and isinstance(month, int) and isinstance(year, int)):
            raise ValueError('Недопустимые значения для даты')
        if year > datetime.MAXYEAR or year < datetime.MINYEAR:
            return False
        if month > 12 or month < 1:
            return False
        if not (1 <= day <= Date.__day_count_dict[month]):
            return False
        if month == 2 and not Date.is_leap_year(year) and day == 29:
            return False
        return True

    @staticmethod
    def is_valid_date(date_str):
        try:
            day, month, year = map(int, date_str.split('-'))
        except ValueError:
            return False
        return Date.is_valid_date_num(day, month, year)

    @classmethod
    def convert_date(cls, date_str):
        if not cls.is_valid_date(date_str):
            raise ValueError('Не удалось сконвертировать строку в число')
        day, month, year = map(int, date_str.split('-'))
        return Date(day, month, year)


print(Date.is_valid_date('29-02-2020'))
print(Date.is_leap_year(2014))
dt = Date(4, 5, 2000)
print(dt)
print(Date.convert_date('1-12-1111'))
