#6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count
from itertools import cycle
from sys import argv

#a)
# generator_script, param_1 = argv
# for el in count(int(param_1)):
#     if el > 20:
#         break
#     else:
#         print(el)

#b)
generator_script_2, param_2 = argv

a = 0
for el in cycle([1, 2, 3]):
    if a > int(param_2):
        break
    else:
        print(el)
    a += 1



