"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


quot = int(input('Введите частное '))
div = int(input('Введите делитель '))
try:
    if div == 0:
        raise ZeroDivision('На ноль делить нельзя.')

    else:
        division = quot / div
        print(division)
except ZeroDivision as err:
        print(err)




