def degree(x, y):
    n = 1
    for i in range(abs(y)):
        n *= x
    return 1 / n


while True:
    try:
        n_1 = float(input("Введите первое положительное число: "))
        n_2 = int(input("Введите отрицательное целое число: "))
        if n_2 >= 0:
            print('Второе число должно быть отрицательным. Попробуйте еще раз')
            continue
    except ValueError:
        print("Ошибка! Необходимо ввести цифрой.Попробуйте еще раз")
        continue
    print(degree(n_1, n_2))
    break
