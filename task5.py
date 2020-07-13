try:
    with open("text_5.txt","w+", encoding="utf-8") as my_file:
        line = input("Введите числа через пробел: ")
        my_file.writelines(line)
        list_num = line.split()
        print(sum(map(int, list_num)))
except ValueError:
    print("Ошибка! Необходимо вводить числа через пробел")
