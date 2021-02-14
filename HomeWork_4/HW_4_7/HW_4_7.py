from itertools import count
from time import sleep
from math import factorial
# from Random_number import list
# # for el in list:
# #     print(el)
def fact():
    for el in count(1):
        # print(el)
        yield factorial(el)
        sleep(0.5)

out_number = fact()
len = int(input('Enter the number of outputted factorials - '))
stop = 0
for i in out_number:
    if stop < len:
        stop += 1
    else:
        break
    print(i)
    sleep(1.5)

