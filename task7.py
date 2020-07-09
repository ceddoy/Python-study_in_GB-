def fact(number):
    f = 1
    for i in range(1, number + 1):
        f *= i
        yield f


n = int(input('Введите число: '))
idx = 1
for el in fact(n):
    print(f'Факториал {idx} равен: {el}')
    idx += 1