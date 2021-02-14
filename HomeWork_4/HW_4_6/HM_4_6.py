# from sys import argv
from itertools import count
from itertools import cycle
from time import sleep

# name, eternity, user_list

eternity = int(input('Enter any number - '))
for el in count(eternity):
    print(el)

user_list = input('Enter few word or symbols - ')
for el in cycle(user_list):
        print(el)
        sleep(0.5)







