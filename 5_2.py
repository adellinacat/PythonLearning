chek = open('fail_2.txt', 'r', encoding='utf-8')
l = chek.read()
print(l)

chek = open('fail_2.txt', 'r', encoding='utf-8')
lines = chek.readlines()
print('количество строк:', len(lines))

chek = open('fail_2.txt', 'r', encoding='utf-8')
lines = chek.readlines()
n=0
for line in lines:
    word = line.split()
    n = n + 1
    print('количество слов', n, '-ой строки', len(word))

chek = open('fail_2.txt', 'r', encoding='utf-8')
l = chek.read()
words = l.split()
print('общее количество слов:', len(words))
chek.close()
