# Определение времени года по месяцу
# Создать список сезонов
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
# Создаем словарь сезонов
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
# Делаем запрос месяца
month = int(input('Введите номер месяца в году: '))
# Вывод сразу обоих вариантов (список/словарь)
if month == 1 or month == 2 or month == 12:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print('Ошибка, не верный месяц!')
