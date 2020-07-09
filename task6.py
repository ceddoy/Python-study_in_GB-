from itertools import count, cycle


def my_func1():
    for el in count(5):
        if el > 8:
            return my_list1
        else:
            my_list1.append(el)


def my_func2():
    i = 0
    for el in cycle("арбуз"):
        if i > 4:
            return my_list2
        my_list2.append(el)
        i += 1


my_list1 = []
print(my_func1())
new_list1 = my_list1.__iter__()
for i in range(len(my_list1)):
    print(new_list1.__next__())

print("*" * 50)

my_list2 = []
print(my_func2())
new_list2 = my_list2.__iter__()
for i in range(len(my_list2)):
    print(new_list2.__next__())