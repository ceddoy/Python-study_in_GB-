import re

my_dict = {}
with open("text_6.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        splitted_line = line.split(':')
        subject = splitted_line[0]
        sum_lessons = sum([int(num) for num in (re.findall('\d+', splitted_line[1]))])
        my_dict[subject] = sum_lessons
print(my_dict)
