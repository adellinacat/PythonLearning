'''Выводит целые числа в указанном диапазоне,
   повторяет элементы списка
'''

from itertools import count, cycle

u_num = int(input('Для запуска введите число: '))

for i in count(u_num):
    fin_num = u_num *2 + 10+1
    if i < fin_num:
        print(i)
    else:
        break
del i
#my_list = [i for i in range(fin_num)]
#count = 0
#for num in cycle(my_list):
 #   if count < fin_num + 10:
  #      print(num)
   #     count += 1
    #else:
     #   break
#print(my_list)
