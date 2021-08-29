class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed} км'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} - {self.speed} км')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенного для городского автомобиля'
        else:
            return f'Скорость {self.name} нормальная для городского автомобиля'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} - {self.speed} км')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из отдела полиции'
        else:
            return f'{self.name} не из отдела полиции'


audi = SportCar(100, 'Красная', 'Ауди', False)
oka = TownCar(30, 'Белая ', 'Ока', False)
lada = WorkCar(70, 'Голубая', 'Лада', True)
ford = PoliceCar(110, 'Синяя',  'Хонда', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, Тогда {audi.stop()}')
print(f'{lada.go()} , {lada.show_speed()}')
print(f'{lada.name} - {lada.color}')
print(f' {audi.name} - полицейская машина? {audi.is_police}')
print(f' {lada.name} -  полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())