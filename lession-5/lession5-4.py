#4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

#в файле lession5-4-test.py решение с помощью дополнительно установленного пакета translate. Про пакет нагуглил, решение сделал сам:)
#потому что то решение, что ниже мне не понравилось

with open("textfile-4.txt") as numb:
    content_new = []
    line = numb.readline()
    key, digit = line.split('-')
    line_new = (f"Один -{digit}")
    content_new.append(line_new)

    line = numb.readline()
    key, digit = line.split('-')
    line_new = (f"Два -{digit}")
    content_new.append(line_new)

    line = numb.readline()
    key, digit = line.split('-')
    line_new = (f"Три -{digit}")
    content_new.append(line_new)

    line = numb.readline()
    key, digit = line.split('-')
    line_new = (f"Четыре -{digit}")
    content_new.append(line_new)

with open("textfile-4-new.txt", "w+", encoding="utf-8") as numb_new:
    numb_new.writelines(content_new)