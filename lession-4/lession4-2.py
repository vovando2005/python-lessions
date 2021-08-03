#2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

parent_list = [200, 15, 38, 11, 26, 17, 299]

i = 0
new_list = []

for el in parent_list:
    if i < len(parent_list) - 1:
        next_el = parent_list[i+1]
        if next_el > el:
           new_list.append(next_el)
    i += 1

print(new_list)

