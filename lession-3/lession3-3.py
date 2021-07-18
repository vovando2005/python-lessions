#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func (var_1, var_2, var_3):
    """
    Возвращает сумму двух наибольших аргументов
    :param var_1: int
    :param var_2: int
    :param var_3: int
    :return: int, сумма двух наибольших аргументов
    """
    a = min(var_1, var_2, var_3)
    result = var_1 + var_2 + var_3 - a
    return result

print(my_func(500,20,30))

