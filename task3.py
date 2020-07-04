def calculation(n_1, n_2, n_3):
    n = [n_1, n_2, n_3]
    n.remove(min(n_1, n_2, n_3))
    return sum(n)


def my_func():
    print(calculation(4, 6, 1))


my_func()
