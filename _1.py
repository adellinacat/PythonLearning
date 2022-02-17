''' Светофор'''

from time import sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def runing(self):
        for key, value in self.__color.items():
            sleep(value)
            print(key)

start = TrafficLight(color={'красный': 2, 'желтый': 7, 'зеленый': 2})
start.runing()
start.runing()
