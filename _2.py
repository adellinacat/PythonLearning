# Запросить у пользователя список элементов, сделать обмен значений соседних элементов

el_num = int(input('Введите количество элементов списка: '))
my_list = []
i = 0
el = 0
while i < el_num:
    my_list.append(input('Введите значение элемента: '))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)