# Вычисление прибыли или убытка фирмы. Если прибыль - добавляем переменную Сотрудники

rev = int(input('Введите выручку: '))
exp = int(input('Введите издержки: '))

pro = (rev - exp)
loss = (rev - exp)
ren = (pro / exp)
if pro > 0:
    print('Прибыль составила: ', pro)
    print('Рентабельность:', ren * 100, '%')
    workers = int(input('Введите количество сотрудников: '))
    print('Прибыль на одного сотрудника: ', pro / workers)
elif pro == 0:
    print('Выручка равна издержкам.')

else:
    print('Убыток составил: ', loss)