from random import randint

my_list = [randint(0, 1000) for i in range(10)]
print(f"Исходный список: {my_list}")
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(f"Измененный список: {new_list}")
