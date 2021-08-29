from time import sleep


class TrafficLight:
    _states = {'красный': 7, 'желтый': 5, 'зеленый': 10}
    _color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color

            print(f"На светофоре загорелся '{self._color}' "f"на {sw_time} секунд")
            sleep(sw_time)


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
