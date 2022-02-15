with open('fail_3.txt', 'r', encoding='utf-8') as data_f:
    j = data_f.read()
    print(j)
with open('fail_3.txt', 'r', encoding='utf-8') as data_f:
    x = []
    y = []
    my_list = data_f.readlines()

    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            y.append(i[0])
        x.append(i[1])
print('Работники с окладом менее 20000руб.: ', y, '\n', 'Средняя зарплата: ', round(sum(map(float, x,)) / len(x)))
