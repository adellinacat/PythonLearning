# Создать список разных типов данных
my_list = [2, 'Hello', 1.1, (1, 2), [5, 5, 6], {1, 11, 111}, True, "fhgfesj"]
# Вывести типы данных
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)
