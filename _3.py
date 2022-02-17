class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income.get('wage') + self._income.get('bonus')


firstworker = Position('Петр', 'Петров', 'разработчик', 190000, 25400)
print(firstworker.get_full_name())
print(firstworker.position)
print(firstworker.get_full_salary())
print('*****************')
secondworker = Position('Иван', 'Иванов', 'инженер', 150000, 13000)
print(secondworker.get_full_name())
print(secondworker.position)
print(secondworker.get_full_salary())
