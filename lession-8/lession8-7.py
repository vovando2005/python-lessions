"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return complex(self.a, self.b) + complex(other.a, other.b)

    def __mul__(self, other):
        return complex(self.a, self.b) * complex(other.a, other.b)

n1 = Complex(2, 3)
n2 = Complex(5, 6)

print(n1 + n2)
print(n1 * n2)


