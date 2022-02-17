class Car:
    name: str
    color: str
    speed: int
    is_police: bool

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
    def go(self):
        return f'поехал'
    def stop(self):
        return  f'остановился'
    def tern_right(self):
        return f'повернул направо'
    def tern_left(self):
        return f'повернул налево'
    def my_speed(self):
        return self.speed
    def my_color(self):
        return self.color
    def my_name(self):
        return self.name

class SportCar(Car):
    def sport_car(self):
        return " - sport car"

class WorkCar(Car):
    def work_car(self):
        if self.speed > 40:
            return f' - превысил скорость'
        else:
            return self.speed

class TownCar(Car):
    def town_car(self):
        if self.speed > 60:
            return  f'превысил скорость'
        else:
            return self.speed

class PoliceCar(Car):
    def police_car(self):
        if self.is_police is True:
            return " - полицейский автомобиль"

gazel = WorkCar('Gazel', 'белая', 40, False)
ford = TownCar('Ford', 'серый', 65, False)
opel = PoliceCar('Opel', 'черный', 100, True)
ferarry = SportCar('Ferarry', 'красный', 120, False)

print(f'Ferarry {ferarry.sport_car()} {ferarry.tern_left()}.')
print(f'Ford {ford.go()}, {ford.tern_right()} и {ford.town_car()}.')
print(f'Gazel {gazel.go()} - его скорость составляет {gazel.work_car()} км/ч, {gazel.tern_right()} и {gazel.stop()}.')
print(f'Opel {opel.tern_left()} cо скоростью {opel.my_speed()} км/ч, но ему так можно это {opel.police_car()}.')
print(f'{opel.my_name()} - {opel.my_color()}, {gazel.my_name()} - {gazel.my_color()}')
