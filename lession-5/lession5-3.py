#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников

with open("textfile_3.txt", encoding="UTF-8") as f_obj:
    i = 0
    sum_salary = 0
    for line in f_obj:
        i += 1
        surname, salary = line.split()
        if int(salary) < 20000:
            print(f"У сотрудника {surname} оклад меньше 20000")
        sum_salary += int(salary)

    avarage_salary = sum_salary / i

    print(f"Средний оклад: {avarage_salary:.2f}")

