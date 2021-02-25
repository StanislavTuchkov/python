from random import *
from colorama import *
class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        if str(self.color).upper() == 'BLUE':
            print(Fore.LIGHTBLUE_EX + f'{self.name}  is moving.')
        if str(self.color).upper() == 'RED':
            print(Fore.RED + f'{self.name}  is moving.')
        if str(self.color).upper() == 'YELLOW':
            print(Fore.LIGHTYELLOW_EX + f'{self.name}  is moving.')
        if str(self.color).upper() != 'BLUE' or str(self.color).upper() != 'RED' or str(self.color).upper() != 'YELLOW':
            print(Fore.LIGHTGREEN_EX + f'{self.name}  is moving.')
    def stop(self):
        print(Fore.RED + 'Car stopped!')

    def turn(self):
        a = randrange(1, 3)
        if a == 1:
            print (Fore.GREEN + '<-left')
        print()
        if a == 2:
            print (Fore.CYAN + 'right->')
    def show_speed(self):
        print(self.speed)
class TownCar(Car):
    # speed = 90
    # color = (Fore.LIGHTYELLOW_EX + 'Yellow')
    # name = 'Ford'
    def show_speed(self):
        if self.speed > 60:
            print('Speed is too high! Decrease speed!')
class SportCar(Car):
    speed = 240
    # color = (Fore.RED + 'Red')
    # name = 'Mustang'
class WorkCar(Car):
    # speed = 100
    # color = (Fore.LIGHTBLACK_EX + 'Black')
    # name = 'GAZ'
    def show_speed(self):
        if self.speed > 40:
            print('Speed is too high! Decrease speed!')

tc = TownCar(100, 'blue', 'GAZ')
tc.go()
tc.show_speed()


