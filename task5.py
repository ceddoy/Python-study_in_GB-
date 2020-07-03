my_list = [8, 7, 7, 5, 2]
num = int(input("Введите число: "))
for i in range(len(my_list)):
    if num > my_list[i]:
        my_list.insert(i, num)
        break
    elif num <= my_list[-1]:
        my_list.append(num)
        break
print(my_list)

