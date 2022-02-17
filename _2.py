class Road:

    def __init__(self, length, width, weight, layer):
        self._length = length
        self._width = width
        self.weight = weight
        self.layer = layer

    def mass(self):
        a = self._length
        b = self._width
        c = self.weight
        d = self.layer
        total = a * b * c * d / 1000
        return print(f'Расход асфальта:\n {a} м * {b} м * {c} кг * {d} см =', total, 'т')

r = Road(20, 5000, 25, 5)
r.mass()
r = Road(10, 10000, 15, 6)
r.mass()
r = Road(9, 10000, 14, 4)
r.mass()
