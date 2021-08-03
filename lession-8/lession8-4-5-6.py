"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

class Storage:
    def __init__(self, max_amount):
        self.max_amount = max_amount

class OfficeEquipment(Storage):

    equipment_dict = {}

    def __init__(self, amount, name):
        self.amount = amount
        self. name = name
        self.piece = "шт."


    def acceptance(self):
        self.amount += 1
        OfficeEquipment.equipment_dict.update({self.name: self.amount})
        return OfficeEquipment.equipment_dict

    def move(self):
        self.amount -= 1
        OfficeEquipment.equipment_dict.update({self.name: self.amount})
        return OfficeEquipment.equipment_dict


class Printer(OfficeEquipment):

    amount = 0

    def __init__(self, name, type, color_or_monochrome):
        # super().__init__(name)
        self.name = name
        self.type = type
        self.color_or_monochrome = color_or_monochrome
        self.own_name = name
        if color_or_monochrome == 'color' or color_or_monochrome == 'monochrome':
            pass
        else:
            print(f'Принтер {self.name} может быть только color или monochrome')


    def acceptance(self):
        self.name = __class__.__name__
        OfficeEquipment.acceptance(self)
        Printer.amount = + 1

    def move(self, move_to):
        self.name = __class__.__name__
        Printer.amount =- 1
        OfficeEquipment.move(self)
        print(f'{__class__.__name__} {self.own_name} отправлен в отдел {move_to}')





class Scaner(OfficeEquipment):

    amount = 0


    def __init__(self, name, format, resolution):
        # super().__init__(name)
        self.format = format
        self.resolution = resolution
        self.own_name = name



    def acceptance(self):
        self.name = __class__.__name__
        OfficeEquipment.acceptance(self)
        Scaner.amount += 1

    def move(self, move_to):
        self.name = __class__.__name__
        Scaner.amount = - 1
        OfficeEquipment.move(self)
        print(f'{__class__.__name__} {self.own_name} отправлен в отдел {move_to}')





class Xerox(OfficeEquipment):

    amount  = 0
    def __init__(self, name, format, color_or_monochrome):
        # super().__init__(name)
        self.format = format
        self.name = name
        self.color_or_monochrome = color_or_monochrome
        self.own_name = name
        if color_or_monochrome == 'color' or color_or_monochrome == 'monochrome':
            pass
        else:
            print(f'Ксерокс {self.name} может быть только color или monochrome')


    def acceptance(self):
        self.name = __class__.__name__
        OfficeEquipment.acceptance(self)
        Xerox.amount += 1

    def move(self, move_to):
        self.name = __class__.__name__
        Xerox.amount =- 1
        OfficeEquipment.move(self)
        print(f'{__class__.__name__} {self.own_name} отправлен в отдел {move_to}')


printer1 = Printer('HP L1100', 'laser', 'monochrome')
scanner1 = Scaner('Canon S515', 'A4', '1900x1500')
xerox1 = Xerox('Xerox X999', 'A4', 'color')
xerox2 = Xerox('Xerox X999', 'A4', 'monodrom')
printer2 = Printer('Canon E95', 'laser', 'mono')
printer1.acceptance()

printer2.acceptance()

scanner1.acceptance()

xerox1.acceptance()
xerox2.acceptance()
print(OfficeEquipment.equipment_dict)
printer2.move('Бухгалтерия')
xerox2.move('Отдел кадров')
scanner1.move('Бухгалтерия')
print(OfficeEquipment.equipment_dict)





