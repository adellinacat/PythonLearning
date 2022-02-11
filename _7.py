'''Генерирует список чисел до 15 и выводит факториалы этих чисел'''

from itertools import count
from math import factorial

def my_func():
    for el in count(1):
        yield factorial(el)

my_gen = my_func()
x = 0
for i in my_gen:
    if x < 15:
        print('факториал ', x + 1, '=', i)
        x += 1
    else:
        break
