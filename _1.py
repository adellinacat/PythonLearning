from datetime import date

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def trans(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != ' ':
                date.append(i)
        return int(date[2]), int(date[1]), int(date[0])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'верно: {year, month,day}'
                else:
                    return f'год неверный'
            else:
                return f'месяц неверный'
        else:
            return f'день месяца неверный'

today = date.today()

print("сегодня: ", today)
#print(today)
print(Data.valid(65, 11, 2022))
print(Data.valid(23, 2, 2020))
print(Data.valid(14, 12, 1990))
print(Data.valid(222, 222, 222))
print(Data.valid(15, 2, 2000))
