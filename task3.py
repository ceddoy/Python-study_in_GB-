class Cell:
    def __init__(self, count):
        self.count = count
        print(f'Клетка с {self.count} ячейками')

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if (self.count - other.count) > 0:
            return self.count - other.count
        else:
            print('Разность клеток меньше нуля')
            return 0

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, line):
        str_1 = ''
        c1 = self.count // int(line)
        c2 = self.count - (c1 * line)
        for i in range(c1):
            for j in range(line):
                str_1 += '*'
            str_1 += '\n'
        for i in range(c2):
            str_1 += '*'
        return str_1


a = Cell(15)
b = Cell(13)
c = Cell(a + b)
d = Cell(a - b)
e = Cell(a * b)
f = Cell(a / b)
print(a.make_order(5))