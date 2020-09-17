from time import sleep, time
from itertools import cycle
print('Задание №1')


class TrafficLight:
    __color = 'red'

    def running(self):
        color_time = {'yellow': 2,
                      'red': 7,
                      'green': 5}
        switch_colors = ['yellow', 'green', 'yellow', 'red']
        tm = time() + 60
        for col in cycle(switch_colors):
            self.__color = col
            print(f'TrafficLight is {col}')
            sleep(color_time[col])
            if time() > tm:
                break


a = TrafficLight()
a.running()
