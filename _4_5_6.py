from datetime import datetime

class Warehouse:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
        t = datetime.now()
        self.lists.update(
            {equipment.title: [equipment.serial_number, str(t.day) + '.' + str(t.month) + '.' + str(t.year)]})
        print('На ' + self.title + ' принято оборудование: ' + '' + equipment.title +
              ', серийный номер: ' + str(equipment.serial_number) + ', Дата: '
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))

    def give_to_depot(self, equipment, other):
        t = datetime.now()
        self.give_lists.update(
            {equipment.title: [equipment.serial_number, str(t.day) + '.' + str(t.month) + '.' + str(t.year)]})
        print('Передано оборудование: ' + '' + equipment.title +
              ', серийный номер - ' + str(equipment.serial_number) + ', Дата: ' + str(t.day) + '.' + str(
            t.month) + '.' + str(t.year))
        other.take_to_depot(equipment)

    def list_equipments(self):
        print('На ' + self.title + ' принято оборудование: ')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада ' + self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))


class OfficeEquipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)


class Printer(OfficeEquipment):
    def __init__(self, title, serial_number, param):
        OfficeEquipment.__init__(self, title, serial_number)
        self.param = param

    def __str__(self):
        return 'Название модели: ' + OfficeEquipment.__str__(self) + ', произв-сть: ' + str(self.param) + ' л/м'


class Scanner(OfficeEquipment):
    def __init__(self, title, serial_number, param):
        OfficeEquipment.__init__(self, title, serial_number)
        self.param = param

    def __str__(self):
        return 'Название модели: ' + OfficeEquipment.__str__(self) + ', разрешение: ' + str(self.param) + ' px'


class Copier(OfficeEquipment):
    def __init__(self, title, serial_number, param):
        OfficeEquipment.__init__(self, title, serial_number)
        self.param = param

    def __str__(self):
        return 'Название модели: ' + OfficeEquipment.__str__(self) + ', произв-ть: ' + str(self.param) + ' л/м'


store1 = Warehouse('Главный склад')
store2 = Warehouse('Подразделение')
a = Printer('Printer Epson', 10.2001, 550)
b = Scanner('Scanner Сanon', 123.456, 4000)
c = Copier('Copier HP', 123456789, 450)

print(a)
print(b)
print(c)
store1.take_to_depot(a)
store1.take_to_depot(b)
store1.take_to_depot(c)
store1.give_to_depot(a, store2)
store1.give_to_depot(c, store2)
store1.list_equipments()
store2.list_equipments()
