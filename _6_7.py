''' Принимает строку из слов строчными буквами,
 возвращает строку из слов с большой буквы '''

def int_func(text):
    if text.replace(" ", "").isalpha():
        return text.title()
    else:
        print('only letters')
s1 = str(input('Enter some text through a space: '))
print(int_func(s1))