def my_func():
    result = 0
    while True:
        user_ans = input("Введите числа через пробел, для выхода введите '*' : ").split()
        for i in list(user_ans):
            try:
                if i == "*":
                    print(f"Выход из программы. Сумма чисел составляет: {result}.")
                    return
                else:
                    result += int(i)
            except ValueError:
                print("Вам необходимо вводить числа, либо ввести '*' для выхода.")
        print(f"Сумма чисел составляет: {result}.")


my_func()
