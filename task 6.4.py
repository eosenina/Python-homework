import random
from itertools import cycle
print('Задание №4')


class Car:
    speed = 0
    color = 'white'
    name = 'car'
    is_police = False

    def go(self):
        self.speed = random.randint(1, 120)
        print('Машина поехала')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class WorkCar(Car):
    def __init__(self, color='yellow'):
        self.color = color
        self.name = 'work car'

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 40:
            print('Скорость превышена!')


class TownCar(Car):
    def __init__(self, color='black'):
        self.name = 'town car'
        self.color = color

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')
        if self.speed > 60:
            print('Скорость превышена!')


class PoliceCar(Car):
    def __init__(self, color='blue'):
        self.is_police = True
        self.name = 'police car'
        self.color = color


class SportCar(Car):
    def __init__(self, color='red'):
        self.name = 'sport car'
        self.color = color


actions = [Car.go, Car.turn, Car.go, Car.stop]
dr = ['налево', 'направо']
cars = [SportCar(), PoliceCar(), WorkCar(), TownCar(), SportCar('purple')]
for car in cars:
    print(car.name, car.color)
    for i, act in enumerate(cycle(actions)):
        if i > 20:
            break
        if act == Car.turn:
            act(car, dr[random.randint(0, 1)])
            continue
        act(car)
        car.show_speed()
