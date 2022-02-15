russuan = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new = []
with open('fail_4.txt', 'r') as my_obj:
    for i in my_obj:
        i = i.split(' ', 1)
        new.append(russuan[i[0]] + ' ' + i[1])
    print(new)

with open('fail_4.txt','w+', encoding='utf-8') as my_obj1:
    my_obj1.writelines(new)

