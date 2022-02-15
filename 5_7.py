import json
profit = {}
pr = {}
prof = 0
average_profit = 0
i = 0
with open('fail_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Средняя прибыль по всем фирмам: {average_profit:.2f}')
    else:
        print(f'Все работают в убыток')
    pr = {'average_profit': round(average_profit)}
    profit.update(pr)
    print(f'Прибыль/убыток каждой компании: {profit}')

with open('fail_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'json-объект: {js_str}')