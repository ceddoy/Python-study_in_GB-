from time import sleep
from itertools import cycle


class TrafficLight:
    __color = cycle(["Red", "Yellow", "Green", "Yellow"])


    def running(self):
        while True:
            iter_color = next(self.__color)
            print(f"Светофор переключается на\n{iter_color}")
            if iter_color == "Red":
                sleep(7)
            elif iter_color == "Yellow":
                sleep(2)
            elif iter_color == "Green":
                sleep(7)


TrafficLight = TrafficLight()
TrafficLight.running()

