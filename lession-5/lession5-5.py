#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("textfile_5.txt", "w+") as my_numb:
    my_numb.write(input('Введите числа через пробел: '))
    my_numb.seek(0)
    content = my_numb.readline()
    my_numb_list = content.split()
    numb_sum = 0
    for i in my_numb_list:
        numb_sum += int(i)
    print(numb_sum)

