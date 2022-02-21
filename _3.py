
class Cell:
    def __init__(self, amt):
        self.amt = int(amt)

    def __str__(self):
        return f'{self.amt * "#"}'

    def __add__(self, other):
        return Cell(self.amt + other.amt)

    def __sub__(self, other):
        return Cell(self.amt - other.amt)

    def __mul__(self, other):
        return Cell(self.amt * other.amt)

    def __truediv__(self, other):
        return Cell(round(self.amt // other.amt))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.amt / cells_in_row)):
            row += f'{"#" * cells_in_row}\\n'
        row += f'{"#" * (self.amt % cells_in_row)}'
        return row

cells1 = Cell(10)
cells2 = Cell(5)
print(cells1)
print(cells2)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells1 / cells2)
print(cells1.make_order(4))
print(cells2.make_order(3))
print(cells1.make_order(3))
print(cells2.make_order(4))