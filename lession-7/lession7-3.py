"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
"""
import math

class Cell:
    def __init__(self, qty):
        self.qty = qty

    def __add__(self, other):
        return self.qty + other.qty

    def __sub__(self, other):
        if self.qty - other.qty > 0:
            return self.qty - other.qty
        else:
            return f"Нельзя выполнить вычитание"

    def __mul__(self, other):
        return self.qty * other.qty

    def __truediv__(self, other):
        return round(self.qty / other.qty)

    def make_order(self, n):
        row_number = math.ceil(self.qty / n)
        row = ''
        for j in range(row_number + 1):
            i = 1
            while True:

                if len(row) - row.count('\n') >= self.qty:
                    break

                if i <= n:
                   row += '*'
                   i += 1

                if i > n:
                    if j != row_number + 1:
                        row += '\n'
                    break

        return row

cell1 = Cell(4)
cell2 = Cell(112)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell2 / cell1)

print(cell2.make_order(13))

