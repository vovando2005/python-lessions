#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

with open('textfile_7.txt', 'r', encoding='utf-8') as firm:
    firm_dict = {}
    i = 0
    all_profit = 0
    for line in firm:
        i += 1
        content = line.split()
        profit = int(content[2]) - int(content[3])
        if profit > 0:
            all_profit += profit
        temp_dict = {content[0]:profit}
        firm_dict.update(temp_dict)
    avarage_profit = all_profit / i
    print_list = [firm_dict, {'Средняя прибыль':avarage_profit}]

print(print_list)

with open('lession5-7.json', 'w', encoding='UTF-8') as write_json:
    json.dump(print_list, write_json, ensure_ascii=False)

