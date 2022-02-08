name = str(input('введите имя: '))
surname = str(input('ведите фамилию: '))
birth = int(input('год рождения: '))
city = str(input('город проживания: '))
email = str(input('электронная почта: '))
phone = int(input('телефон: '))

def param_user():
    user_dict = {"Имя": name, "Фамилия": surname, "Год рождения": birth, "Город проживания": city, "Email": email, "Телефон": phone}
    return user_dict
print(param_user())

