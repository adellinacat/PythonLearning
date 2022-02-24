class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print('Сумма комплексных чисел')
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print('Произведение комплексных чисел')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.a * other.b + (self.b * other.a)}i'

    def __str__(self):
        print('Комплексное число')
        return f'z = {self.a} + {self.b}i'

z1 = Complex(-2, 2)
z2 = Complex(5, 3)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)



