class Stationery:

    def __init__(self, title):
        self.title = title
    def start(self):
        return f'Начинаем рисовать'

class Pen(Stationery):
    def draw(self):
        return f'инструментом 1 - {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'инструментом 2 - {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'инструментом 3 - {self.title}'

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('кисть')

print(f'{pen.start()} {pen.draw()}')
print(f'{pencil.start()} {pencil.draw()}')
print(f'{handle.start()} {handle.draw()}')