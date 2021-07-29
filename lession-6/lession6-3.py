#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров)

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.__income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        return (f"{self.surname} {self.name}")

    def get_total_income(self):
        income = self.__income
        return int(income.get("wage")) + int(income.get("bonus"))

p_1 = Position("Alex", "Mann", "CEO", 15000, 3000)

print(p_1.get_full_name())
print(p_1.get_total_income())

p_2 = Position('Wilfred', 'Gon', 'IT', 22000, 2000)

print(p_2.get_full_name())
print(p_2.get_total_income())



