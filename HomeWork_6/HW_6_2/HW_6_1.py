from colorama import Fore
class Road:
    __length = 0
    __width = 0

    def weight(self, length=0, width=0, meter_weight_1cm=0, thickness=0):
        a = input(Fore.GREEN + 'Enter S to start or Q to quit - ').upper()
        if a == 'S':
            self.__length = length
            self.__width = width
            self.meter_weight_1cm = meter_weight_1cm
            self.thickness = thickness
            print(Fore.LIGHTYELLOW_EX + f'{length * width * (thickness * meter_weight_1cm) / 1000} tons')
        elif a == 'Q':
            print(Fore.RED + 'Counting stopped')
        else:
            print(Fore.CYAN + 'Enter correct word!!!')

length = int(input('Enter length m - '))
width = int(input('Enter width m - '))
meter_weight_1cm = int(input('Enter meter weight kg - '))
thickness = int(input('Enter thickness cm - '))
a = Road()
a.weight(length, width, meter_weight_1cm, thickness)
print(a.thickness)
