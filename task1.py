def division(dividend, divider):
    try:
        quotient = round(dividend / divider, 3)
        print(f"{dividend} делить на {divider} равно {quotient}")
    except ZeroDivisionError:
        print("На ноль делить нельзя")


while True:
    try:
        num_1 = float(input("Введите первое число: "))
        num_2 = float(input("Введите второе число: "))
        division(num_1, num_2)
        break
    except:
        print("Ошибка! Необходимо вводить число.")
