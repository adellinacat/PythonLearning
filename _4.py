# Найти самую большую цифру в числе
a = int(input('Введите число:'))

if a > 0:
    x = a % 10
    a = a // 10
    while a > 0:
        if x < a % 10:
            x = a % 10
        a = a // 10
    print('максимальное число:', x)
else:
    print('ошибка')