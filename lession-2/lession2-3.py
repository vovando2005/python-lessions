month = int(input('Введите номер месяца: '))

# решение через словарь
month_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
              10: 'осень', 11: 'осень', 12: 'зима'}

for i in month_dict:
    if month == i:
        print(month_dict.get(i))

# решение через список
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month in winter:
    print("зима")
elif month in spring:
    print("весна")
elif month in summer:
    print("лето")
elif month in autumn:
    print("осень")
