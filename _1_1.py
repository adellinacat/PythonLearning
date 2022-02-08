def my_f():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        result = num_1 / num_2
        return result
    except ZeroDivisionError:
        return "Попытка деления на ноль"
print(my_f())

