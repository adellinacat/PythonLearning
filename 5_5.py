def sum_f():
    try:
        with open('fail_5.txt', 'w+') as new_f:
            line_f = input('Введите числа через пробел: ')
            new_f.writelines(line_f)
            num = line_f.split()

        print(sum(map(float, num)))
    except ValueError:
        print('Ошибка ввода:')
sum_f()