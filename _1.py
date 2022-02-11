from sys import argv

script_name, pr_in_hours, rate, bonus = argv
print('Выработка: ', pr_in_hours, 'часов')
print('Ставка: ', rate, 'денег в час')
print('Премия: ', bonus, 'денег')
result = int(pr_in_hours) * int(rate) + int(bonus)
print('Заработная плата: ', result, 'денег')