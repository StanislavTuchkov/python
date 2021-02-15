from random import randrange
ran1 = randrange(1, 7)
list = []
i = 0
random = ran1
while i < random:
    ran2 = randrange(0, 10)
    list.append(ran2)
    i += 1
    if i == random:
        break