translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_list = []
with open('text_4.txt', 'r', encoding="utf-8") as my_file:
    for line in my_file.read().split('\n'):
        line = line.split(' ', 1)
        new_list.append(translate[line[0]] + '  ' + line[1])
    print(new_list)

with open('file_4_new.txt', 'w', encoding="utf-8") as new_file:
    new_file.writelines(new_list)
