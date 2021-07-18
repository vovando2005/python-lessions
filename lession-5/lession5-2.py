#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("textfile_2.txt", "w+") as f_obj:
    content = ['string one\n', 'string two\n', 'string three the end\n']
    f_obj.writelines(content)
    f_obj.seek(0)
    i_lines = 0
    for line in f_obj:
        i_lines += 1
        i_words = len(line.split())
        print(f"Слов в строке {i_lines}: {i_words}")
    print(f"Количество строк в файле: {i_lines}")
