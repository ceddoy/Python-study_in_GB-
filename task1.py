class Matrix:
    def __init__(self, mylist):
        self.mylist = mylist


    def __add__(self, other):
        matrix_new = []
        while True:
            if len(self.mylist) > len(other.mylist):
                other.mylist.append([0])
            elif len(self.mylist) < len(other.mylist):
                self.mylist.append([0])
            else:
                break
        for i in range(len(self.mylist)):
            while True:
                if len(self.mylist[i]) > len(other.mylist[i]):
                    other.mylist[i].append(0)
                elif len(self.mylist[i]) < len(other.mylist[i]):
                    self.mylist[i].append(0)
                else:
                    break
            tmp = []
            for j in range(len(self.mylist[i])):
                tmp.append(self.mylist[i][j] + other.mylist[i][j])
            matrix_new.append(tmp)
        return Matrix(matrix_new)

    def __str__(self):
        return str('\n'.join([' '.join([f"{j:4d}" for j in i]) for i in self.mylist]))

a = [[5, 4, 2, 6], [34, 9, 3]]
b = [[1, 6, 5, 18], [1, 3]]
matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(matrix_1 + matrix_2)