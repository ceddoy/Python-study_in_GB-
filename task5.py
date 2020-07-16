class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручку')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())