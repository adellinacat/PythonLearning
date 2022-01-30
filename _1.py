# Простой калькулятор

operation = input('''Введите тип операции для вычисления:
+ сложение
- вычитание
* умножение
/ деление 
''')
num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
if operation == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)
elif operation == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)
elif operation == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
elif operation == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
else:
    print('Вы ввели не верное значение операции')
