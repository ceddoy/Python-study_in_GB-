class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._widht = width

    def count(self):
        mass1km2 = 5
        thickness_cover = 25
        self.mass = self._lenght * self._widht * mass1km2 * thickness_cover / 1000
        print(f"Общая масса полотна составит: {self.mass} т.")


data = Road(5000, 20)
data.count()
