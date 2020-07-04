def result_data(**kwargs):
    """
    Функция, которая принимает в себя именнованные аргументы,
    тут вариантов использования в одну строку много, но я решил
    использовать цикл с форматированием строки
    """
    result = "; ".join(f"{key}: {val}" for key, val in kwargs.items())
    return result


def user_data():
    print(result_data(name_user=input("Введите ваше имя: "),
                      surname_user=input("Введите вашу фамилю: "),
                      date_birth_user=input("Введите дату рождения (например: 11.11.1111): "),
                      city_user=input("Введите город (деревня, село и т.д.) проживания: "),
                      email_user=input("Введите вашу электронную почту: "),
                      telephone_user=input("Введите номер вашего телефона: ")))


user_data()
