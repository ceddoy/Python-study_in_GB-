from random import randint

my_list = [randint(0, 10) for i in range(10)]
print(f"Исходный список: {my_list}")
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Cписок c уникальными числами: {new_list}")