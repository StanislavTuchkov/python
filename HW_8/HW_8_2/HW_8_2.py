from colorama import Fore
class MyEsception:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        try:
            print(self.a / self.b)
        except TypeError:
            print('Please enter a number not a text')
        except ZeroDivisionError:
            print(Fore.RED + 'ERROR')

num = MyEsception(2344, 0 )