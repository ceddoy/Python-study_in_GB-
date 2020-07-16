from random import choice


class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polise

    def go(self):
        print("Врум, врум, врум...Поехали!")

    def stop(self):
        print("Тормози машинка.")

    def turn(self):
        direction = ["направо", "налево"]
        print(f"Поворачиваем {choice(direction)}")

    def show_speed(self):
        print(f"Ваша скорость сейчас составляет: {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Ваша скорость составляет: {self.speed} км/ч, "
                  f"вы превышаете норму городского автомобиля на {self.speed - 60} км/ч.")
        else:
            print(f"Ваша скорость сейчас составляет: {self.speed} км/ч.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Ваша скорость составляет: {self.speed} км/ч, "
                  f"вы превышаете норму рабочего автомобиля на {self.speed - 40} км/ч.")
        else:
            print(f"Ваша скорость сейчас составляет: {self.speed} км/ч.")


class PoliceCar(Car):
    pass


formula = SportCar(120, "Красная", "Формула 1", False)
gazel = WorkCar(59, "Белая", "Газель", False)
yaz = PoliceCar(90, "Бело-синяя", "УАЗ Патриот", True)
toyota = TownCar(69, "Черная", "Toyota", False)
print(f"Вы сели в {toyota.name}")
toyota.go()
toyota.turn()
toyota.turn()
toyota.show_speed()
toyota.stop()
print(toyota.is_police)

