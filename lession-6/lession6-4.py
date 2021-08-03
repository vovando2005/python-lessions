#4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def show_speed(self):
        print(f"Current speed of {self.color} {self.name}: {self.speed}")

    def go(self):
        if int(self.speed) > 0:
            print(f'{self.color} {self.name} is move')

    def stop(self):
        if int(self.speed) == 0:
            print(f'{self.color} {self.name} stopped')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} turn to {self.direction}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Speed of {self.color} {self.name} exceeding!")

class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
             print(f"Speed of {self.color} {self.name} exceeding!")

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def polise_on_road(self):
       if self.is_police == True:
          print("Cops on road!")


tc1 = TownCar(42, "red", "Hyundai")
tc1.show_speed()

sc1 = SportCar(100, "green", "Lamborghini")
sc1.show_speed()
sc1.go()


pc1 = PoliceCar(100, "blue", "Audi")
pc1.polise_on_road()

wc1 = WorkCar(61, "orange", "ZIL")
wc1.show_speed()
wc1.turn("left")



