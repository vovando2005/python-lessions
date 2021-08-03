#5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''

    def draw(self):
        print('Draw start')

class Pen(Stationery):

    def draw(self):
        print('Pen drawing')

class Pencil(Stationery):

    def draw(self):
        print('Pencil drawing')


class Handle(Stationery):

    def draw(self):
        print('Handle drawing')

pen_1 = Pen()
pen_1.draw()

pencil_1 = Pencil()
pencil_1.draw()

handle_1 = Handle()
handle_1.draw()