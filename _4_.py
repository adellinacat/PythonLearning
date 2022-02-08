''' Возведение числа X в степень Y, при Y отрицательном значении'''

x, y, = float(input('x = ')), int(input('y = '))
def my_func(x, y):
     b = x ** y
     return 1 / b
print(my_func(x, y))

