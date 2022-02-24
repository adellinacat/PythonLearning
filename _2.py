class DivisionByNull:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divide_by_null(divident, divider):
        try:
            return round(divident / divider, 2)
        except:
            return (f"на ноль делить нельзя")


div = DivisionByNull(10, 500)

print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(500, 0.14))
print(div.divide_by_null(100, 45.89))
print(div.divide_by_null(0, 15))