# Запросить несколько слов через пробел и вывести каждое с новой строки
my_st = input('Введите несколько слов через пробел: ')
word = []
num = 1
for el in range(my_st.count(' ') + 1):
    word = my_st.split()
    if len(str(word)) <= 10:
        print(f'{num} {word[el]}')
        num += 1
    else:
        print(f'{num} {word[el][0:10]}')
        num += 1
