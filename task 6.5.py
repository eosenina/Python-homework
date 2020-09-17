print('Задание №5')


class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print('Запустить отрисовку')


class Pen(Stationery):
    def __init__(self):
        self.title = 'ручка'

    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'карандаш'

    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def __init__(self):
        self.title = 'маркер'

    def draw(self):
        print('Отрисовка маркером')


items = [Pen(), Pencil(), Handle()]
for i in items:
    print(f'Запускаем {i.title}:')
    i.draw()
