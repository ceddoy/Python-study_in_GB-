class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя и фамилия: {self.name + " " + self.surname}')

    def get_total_income(self):
        print(f'Ваш доход составляет: {sum(self._income.values())}')

a = Position("Андрей", "Багров", "Юрист", 40000, 5000)
a.get_full_name()
print(f"Ваша должность: {a.position}")
a.get_total_income()