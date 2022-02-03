
# Рейтинг, список, в котором совпадающее число помещается после совпадений в списке
my_list = [7, 6, 6, 5, 4]
print(f'Рейтинг - {my_list}')
x = int(input('Введите число: '))
while x != 11:
    for el in range(len(my_list)):
        if my_list[el] == x:
            my_list.insert(el + 1, x)
            break
        elif my_list[0] < x:
            my_list.insert(0, x)
        elif my_list[-1] > x:
            my_list.append(x)
        elif my_list[el] > x and my_list[el + 1] < x:
            my_list.insert(el + 1, x)
        print(f'Текущий список - {my_list}')
        x = int(input('Введите число: '))
