
class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def consumption(self):
        return self.size / 6.5 + 0.5

    def consumption1(self):
        return self.height * 2 + 0.3

    @property
    def cons_total(self):
        return (f'общий расход ткани на пошив: {round(self.size / 6.5 + 0.5 + self.height * 2 + 0.3)} м')

class Coat(Clothes):

    def __init__(self, size, height):
        super().__init__(size, height)
        self.consumption = round(self.size / 6.5 + 0.5, 2)
    def __str__(self):
        return f'на размер {self.size} расход ткани на пальто: {self.consumption} м'


class Suit(Clothes):

    def __init__(self, size, height):
        super().__init__(size, height)
        self.consumption1 = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'на рост {self.height} м расход ткани на костюм: {self.consumption1} м'


coat = Coat(50, 1.85)
suit = Suit(50, 1.85)
print(coat)
print(suit)
print(coat.cons_total)



