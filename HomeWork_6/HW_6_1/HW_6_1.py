from time import sleep
from colorama import Fore, Back, Style
from tkinter import *

class TrafficLight:
    __color = 0

    def running(self):
        while True:
            # root = Tk()
            # c = Canvas(root, width=100, height=300, bg='black')
            # c.pack()
            # c.create_oval(35, 30, 75, 70, fill='red')
            # root.mainloop()
            # sleep(2)
            #
            # root = Tk()
            # c = Canvas(root, width=100, height=300, bg='black')
            # c.pack()
            # c.create_oval(35, 100, 75, 140, fill='yellow')
            # sleep(2)
            # root.mainloop()
            print(Fore.RED + 'RED')
            sleep(7)
            print(Fore.LIGHTYELLOW_EX + "YELLOW")
            sleep(2)
            print(Fore.GREEN + Style.DIM + "GREEN")
            sleep(7)

a = TrafficLight()
a.running()
