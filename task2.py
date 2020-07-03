count = int(input("Какое число элементов вы хотите внести в список: "))
list_number = []
while count > 0:
    data_input = input(f"Осталось внести в список {count} элемент(а/ов), вносите: ")
    list_number.append(data_input)
    count -= 1
print(f" Исходный список:{list_number}")
for i in range(1, len(list_number), 2):
    list_number[i], list_number[i - 1] = list_number[i - 1], list_number[i]
print(f" Измененный список:{list_number}")
