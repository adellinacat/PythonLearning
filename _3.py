class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Вводите числа по одному и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Ваш список: {self.my_list} \n ')
            except:
                print(f'Недопустимое значение: требуется вводить число')
                stop = input(f'Попробовать снова? Выберите: Y/N ')

                if stop == 'Y' or stop == 'y':
                    print(try_except.my_input())
                elif stop == 'N' or stop == 'n':
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())
