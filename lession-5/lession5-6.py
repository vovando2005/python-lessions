#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.


import re
#для вычленения чисел из строки нагуглил такой метод с помощью регулярных выражений.
# s = input()
#
# nums = re.findall(r'\d+', s)
#
# nums = [int(i) for i in nums]

with open("textfile_6.txt", "r", encoding="utf-8") as disciples:
    disciples_dict = dict()
    for line in disciples:
        disciple, hours = line.split(':')
        nums = re.findall(r'\d+', hours)
        nums = [int(i) for i in nums]
        all_hours = sum(nums)
        temp_dict = {disciple : all_hours}
        disciples_dict.update(temp_dict)
    print(disciples_dict)
