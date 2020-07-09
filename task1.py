from sys import argv


def salary(tm, rt, pm):
    return (tm * rt) + pm


try:
    time, rate, premium = map(float, argv[1:])
    print(f"Ваша заработная плата составляет: {salary(time, rate, premium)}")
except ValueError:
    print("Необходимо вводите числа в таком порядке через пробел: \nвыработка в часах, ставка в час, премия")
