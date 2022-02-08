def user_sum ():
    global exit
    i = input('Введите числа через пробел или # для завершения ').split()
    a = 0
    for el in range(len(i)):
        if i[el] == '#':
            exit = True
            break
        else:
            a = a + int(i[el])
    return(a)

exit = False
result = 0
while exit == False:
    result = result + user_sum()
    if exit == False:
        print('Промежуточный результат: ', result, 'можно продолжить ввод.')
    else:
        print('Завершение программы, окончательнеый результат: ', result)