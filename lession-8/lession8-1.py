"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        Date.date = f'{day}-{month}-{year}'

    @classmethod
    def date_date(cls):
        date_list = cls.date.split('-')
        day_int = int(date_list[0])
        month_int = int(date_list[1])
        year_int = int(date_list[2])
        print(f'число {day_int}\n'
              f'месяц {month_int}\n'
              f'год {year_int}')

    @staticmethod
    def date_valid(day, month, year):
        if day > 0 and day < 31:
            print(day)
        else:
            print("День введен некорректно")
        if month > 0 and month <= 12:
            print(month)
        else:
            print("Месяц введен некорректно")
        if year >= 1900 and year <= 2100:
            print(year)
        else:
            print("Год введен некорректно")






date1 = Date(3, 10, 2000)

date1.date_date()

Date.date_valid()

