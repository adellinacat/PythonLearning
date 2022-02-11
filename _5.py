''' Выводит список всех четных чисел от 100 до 1000
    Выводит результат произведения всех элементов списка
'''
from functools import reduce

my_list = [i for i in range(100, 1002) if i % 2 == 0]
print('Список четных чисел ', my_list)
mult = reduce((lambda x, y: x * y), my_list)
print('Произведение чисел = ', mult)
