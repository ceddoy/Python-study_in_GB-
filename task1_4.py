num = int(input("Введите число: "))
a = num % 10
num = num // 10
while num > 0:
    if a == 9:
        break
    elif num % 10 > a:
        a = num % 10
    num //= 10
print(f"Самое большое число в цифре: {a}")
print("Конец программы")
