from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parametr):
        self.parametr = parametr

    @abstractmethod
    def count_cloth(self):
        pass


class Coat(Clothes):
    @property
    def count_cloth(self):
        print(f"Расход ткани на костюм составляет: {round(self.parametr / 6.5 + 0.5, 3)} метров.")
        return self.parametr / 6.5 + 0.5


class Costume(Clothes):
    @property
    def count_cloth(self):
        print(f"Расход ткани на костюм составляет: {round(2 * self.parametr + 0.3, 3)} метров.")
        return 2 * self.parametr + 0.3


while True:
    try:
        v = float(input("Введите размер для пальто: "))
        h = float(input("Введите рост клиента в метрах для костюма: ").replace(',', '.'))

        print(f"Общий расход ткани составляет: {round(Coat(v).count_cloth + Costume(h).count_cloth, 3)} метров.")

        break

    except ValueError:
        print("На ввод допускаются только целые и дробные числа. Попробуйте снова.")
