fname = input('Имя: ')
sname = input('Фамилия: ')
salary = input('Зарплата: ')
str_list = [fname, sname, salary]

with open(fname, 'w+') as f_obj:
    f_obj.write(fname + '\n' + sname + '\n' + salary + '\n')
    while True:
        s = input()
        if s == '':
            break
        f_obj.write(s+'\n')
print(str_list)

